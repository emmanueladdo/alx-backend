import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const app = express();
const port = 1245;
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

// Data
const listProducts = [
  {
    itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4,
  },
  {
    itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10,
  },
  {
    itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2,
  },
  {
    itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5,
  },
];

// Data access
const getItemById = (id) => listProducts.find((item) => item.itemId === id);

// Server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

// Products
app.get('/list_products', (req, res) => {
  res.json(listProducts.map((item) => ({
    itemId: item.itemId,
    itemName: item.itemName,
    price: item.price,
    initialAvailableQuantity: item.initialAvailableQuantity,
  })));
});

// In stock in Redis
const reserveStockById = (itemId, stock) => {
  client.set(`item.${itemId}`, stock);
};

const getCurrentReservedStockById = async (itemId) => {
  const reservedStock = await getAsync(`item.${itemId}`);
  return reservedStock ? parseInt(reservedStock) : 0;
};

// Product detail
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);

  if (item) {
    const currentQuantity = item.initialAvailableQuantity - await getCurrentReservedStockById(itemId);
    res.json({ ...item, currentQuantity });
  } else {
    res.json({ status: 'Product not found' });
  }
});

// Reserve a product
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
    res.json({ status: 'Product not found' });
    return;
  }

  const currentQuantity = item.initialAvailableQuantity - await getCurrentReservedStockById(itemId);

  if (currentQuantity <= 0) {
    res.json({ status: 'Not enough stock available', itemId });
  } else {
    reserveStockById(itemId, currentQuantity - 1);
    res.json({ status: 'Reservation confirmed', itemId });
  }
});
