import { createClient } from 'redis';
import { promisify } from 'util';

const express = require('express');

const listProducts = [{
  id: 1, name: 'Suitcase 250', price: 50, stock: 4,
},
{
  id: 2, name: 'Suitcase 450', price: 100, stock: 10,
},
{
  id: 3, name: 'Suitcase 650', price: 350, stock: 2,
},
{
  id: 4, name: 'Suitcase 1050', price: 550, stock: 5,
}];
function getItemById(id) {
  return listProducts.find((product) => product.id === id);
}
const app = express();
const port = 1245;

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

const client = createClient();
client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));

function reserveById(itemId, stock) {
  client.set(`item.${itemId}`, stock);
}
async function getCurrentReservedStockById(itemId) {
  const Async = promisify(client.get).bind(client);
  const res = await Async(`item.${itemId}`);
  return res;
}
app.get('/list_products', (req, res) => {
  res.send(listProducts.map((product) => ({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
  })));
});
app.get('/list_products/:itemId', async (req, res) => {
  const { itemId } = req.params;
  const product = getItemById(Number(itemId));
  if (product === undefined) {
    res.status(404).send({ status: 'Product not found' });
  } else {
    const reserve = await getCurrentReservedStockById(product.id);
    res.send({
      itemId: product.id,
      itemName: product.name,
      price: product.price,
      initialAvailableQuantity: product.stock,
      currentQuantity: reserve === null ? product.stock : Number(reserve),
    });
  }
});
app.get('/reserve_product/:itemId', async (req, res) => {
  const { itemId } = req.params;
  const product = getItemById(Number(itemId));
  if (product === undefined) {
    res.status(404).send({ status: 'Product not found' });
  }
  let reserve = await getCurrentReservedStockById(product.id);
  reserve = reserve === null ? product.stock : Number(reserve);
  if (!reserve) {
    res.send({ status: 'Not enough stock available', ItemId: product.id });
  } else {
    reserveById(product.id, reserve - 1);
    res.send({ status: 'Reservation confirmed', ItemId: product.id });
  }
});
app.listen(port, () => {
  console.log(`app listening on port ${port}`);
});
