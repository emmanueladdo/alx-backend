// Function the sums two number and returns sum
const Utils = {
  calculateNumber(type, a, b) {
    switch (type) {
      case 'SUM':
        return Math.round(a) + Math.round(b);
      case 'SUBTRACT':
        return Math.round(a) - Math.round(b);
      case 'DIVIDE':
        if (Math.round(b) !== 0) {
          return Math.round(a) / Math.round(b);
        }
        return 'Error';

      default:
        return 'Invalid operation';
    }
  },
};

module.exports = Utils;
