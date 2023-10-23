const { getTopPerformers } = require('./index');

test('fetches top-performing players', async () => {
  const performers = await getTopPerformers();
  expect(performers.length).toBeGreaterThan(0);
  expect(performers[0]).toHaveProperty('name');
  expect(performers[0]).toHaveProperty('points');
});
