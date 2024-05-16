function nerdify(text) {
  //turn nunbers into text
  // Print each letter from the input string individually
  // Replace a's with 4's
  // Replace e's with 3's
  // Replace l's & i's with 1's
  const replacements = {
    a: "4",
    A: "4",
    e: "3",
    E: "3",
    l: "1",
    L: "1",
    i: "1",
    I: "1",
  };

  let result = "";
  for (let char of text) {
    result += replacements[char] || char;
    console.log("Characters:", replacements);
  }

  return result;
}
