#!/usr/bin/node
exports.esrever = function (list) {
  const nbr = list.length;
  for (let i = 0; i < nbr / 2; i++) {
    const temp = list[i];
    list[i] = list[nbr - i - 1];
    list[nbr - i - 1] = temp;
  }
  return (list);
};
