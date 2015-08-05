var fs = require('fs');
var cesar = require('./cesar');
var transp = require('./transp');

if (process.argv.length < 6) {
  return;
}

var algo = process.argv[2];
var op = process.argv[3];
var entrada = process.argv[4];
var chave = process.argv[5];

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

fs.open(entrada, "r", function(err, f) {
  if (err) {
    return;
  }

  fs.readFile(entrada, function(err, data) {
    if (err) {
      return;
    }

    data = data.toString();

    switch(algo) {
      case "cesar":
        var codigo = cesar[op](data, parseInt(chave, 10));

        var saida = "cesar_" + op + ".txt";
        gravaSaida(saida, codigo);
        break;
      case "transp":
        var codigo = transp[op](data, parseInt(chave, 10));

        var saida = "transp_" + op + ".txt";
        gravaSaida(saida, codigo);
        break;
    }
  });
});
