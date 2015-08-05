var fs = require('fs');
var cesar = require('./cesar');
var transp = require('./transp');

if (process.argv.length < 6) {
  return;
}

var algorithm = process.argv[2];
var op = process.argv[3];
var file = process.argv[4];
var key = process.argv[5];

function gravaSaida(filename, codigo) {
  fs.open(filename, "w+", function(err, fd) {
    if (err) {
      return;
    }

    fs.write(fd, codigo, 0, codigo.length, function(err, written, buffer) {
      if (err) {
        return;
      }
    });
  });
}

fs.open(file, "r", function(err, f) {
  if (err) {
    return;
  }

  fs.readFile(file, function(err, data) {
    if (err) {
      return;
    }

    data = data.toString();

    switch(algorithm) {
      case "cesar":
        var codigo = cesar[op](data, parseInt(key, 10));

        var saida = "cesar_" + op + ".txt";
        gravaSaida(saida, codigo);
        break;
      case "transp":
        var codigo = transp[op](data, parseInt(key, 10));

        var saida = "transp_" + op + ".txt";
        gravaSaida(saida, codigo);
        break;
    }
  });
});
