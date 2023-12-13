#!/usr/bin/node
exports.esrever = function (list) {
  const revlist = [];
  const nbr = list.length;

  for (let i = nbr - 1, j = 0; i >= 0; i--, j++) {
    revlist[j] = list[i];
  }
};
