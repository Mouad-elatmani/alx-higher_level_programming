#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && !isNaN(w) && h > 0 && !isNaN(h)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let result = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) { result += 'X'; }
      if (i < this.height - 1) { result += '\n'; }
    }
    console.log(result);
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
