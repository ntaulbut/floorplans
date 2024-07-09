/*
At: http://buildinginformation.nottingham.ac.uk/.
Run this code in the browser console.
The result will be an Object mapping building names to their codes.
Your browser console should let you copy this Object as JSON.
Make sure you are inspecting the right `iframe`.
*/

var codes = Array.from(
  document.querySelectorAll("table:nth-of-type(2) tr:not(.tabletitle) td:nth-of-type(1)")
).map(v => Number(v.innerText))

var names = Array.from(
  document.querySelectorAll("table:nth-of-type(2) tr:not(.tabletitle) td:nth-of-type(2)")
).map(v => v.innerText)

Object.fromEntries(names.map((v, i) => [v, Number(codes[i])]))
