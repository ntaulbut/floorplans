var codes = Array.from(
  document.querySelectorAll("table:nth-of-type(2) tr:not(.tabletitle) td:nth-of-type(1)")
).map(v => Number(v.innerText))

var names = Array.from(
  document.querySelectorAll("table:nth-of-type(2) tr:not(.tabletitle) td:nth-of-type(2)")
).map(v => v.innerText)

Object.fromEntries(names.map((v, i) => [v, Number(codes[i])]))
