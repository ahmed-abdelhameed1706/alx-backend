import redis from "redis";

const client = redis.createClient();

client.on("connect", function () {
  console.log("Redis client connected to the server");
});

client.on("error", function (err) {
  console.error(`Redis client not connected to the server: ${err}`);
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, function (err, reply) {
    if (err) {
      console.error(err);
    } else {
      console.log(reply);
    }
  });
}

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
