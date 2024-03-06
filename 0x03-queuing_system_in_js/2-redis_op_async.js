import redis from "redis";
import { promisify } from "util";

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

client.on("connect", function () {
  console.log("Redis client connected to the server");
});

client.on("error", function (err) {
  console.error(`Redis client not connected to the server: ${err}`);
});

async function setNewSchool(schoolName, value) {
  await setAsync(schoolName, value);
  console.log("Reply: OK");
}

async function displaySchoolValue(schoolName) {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (err) {
    console.error(err);
  }
}

(async () => {
  await displaySchoolValue("Holberton");
  await setNewSchool("HolbertonSanFrancisco", "100");
  await displaySchoolValue("HolbertonSanFrancisco");
  client.quit();
})();
