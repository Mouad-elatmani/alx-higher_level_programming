#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let cnt = 0;
  for (const elem of list) {
    if (elem === searchElement) { cnt++; }
  }
  return cnt;
};
