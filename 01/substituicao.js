var fs = require('fs');

module.exports = {
  cifra: function(string, chave) {
    var newData = "";

    for (var i = 0; i < string.length; i++) {
      newData += String.fromCharCode(chave[string.charCodeAt(i)])
    }

    return newData;
  },
  decifra: function(string, chave) {
    var newData = "";

    for (var j = 0; j < string.length; j++) {
      var val = string.charCodeAt(j);
      for (var i in chave) {
        if (!chave.hasOwnProperty(i)) {
          continue;
        }

        if (val != chave[i]) {
          continue;
        }

        newData += String.fromCharCode(i);
      }
    }

    return newData;
  },
  chave: function(filename, callback) {
    var chave = {};

    fs.open(filename, "r", function(err, fd) {
      if (err) {
        return process.exit();
      }

      while(1) {
        var c = new Buffer(10);

        // ultima linha
        if (fs.readSync(fd, c, 0, 4, null) <= 3) {
          break;
        }

        c = c.toString().substr(0, 3);
        p = c.split(",");
        chave[p[0].charCodeAt()] = p[1].charCodeAt();
      }

      callback(chave);
    });
  }
}
