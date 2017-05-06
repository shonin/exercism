class Bob {
  hey(message) {
    if (message.includes('?')) {
      return 'Sure.';
    }
    if (!/[A-z]+/.test(message)) { return 'Whatever.'}
    if (message.toUpperCase() === message) {
        return 'Whoa, chill out!'
    } 
    return 'Whatever.';
  }
}

export default Bob;
