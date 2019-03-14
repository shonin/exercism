// why does .setUTCSeconds work but .setSeconds doesn't, for the final solution?

let gigasecond = (input) => {
  let birthDateTime = new Date(input);
  return new Date(birthDateTime.setUTCSeconds(birthDateTime.getSeconds() + 10**9));
};

export { gigasecond };
