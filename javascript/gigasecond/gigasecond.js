// # Gigasecond
// Calculate the moment when someone has lived for 10^9 seconds.
// A gigasecond is 10^9 (1,000,000,000) seconds.

let gigasecond = (input) => {
  let birthDateTime = new Date(input);
  return new Date(birthDateTime.setSeconds(birthDateTime.getSeconds() + 10**9))
};

export { gigasecond };
