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

// Fetch the current gameweek information
async function getCurrentGameweek() {
  try {
    const response = await axios.get(`${FPL_API_URL}/events`);
    return response.data.filter(gw => gw.is_current)[0];
  } catch (error) {
    console.error("Error fetching current gameweek:", error);
  }
}

module.exports = { getTopPerformers, getCurrentGameweek };

