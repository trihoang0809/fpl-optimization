const axios = require('axios');

const FPL_API_URL = "https://api.fpl.com/data";

// Fetch current top-performing players
async function getTopPerformers() {
  try {
    const response = await axios.get(`${FPL_API_URL}/top-players`);
    return response.data;
  } catch (error) {
    console.error("Error fetching top performers:", error);
  }
}

// ... Other API calls and operations ...

module.exports = { getTopPerformers };
