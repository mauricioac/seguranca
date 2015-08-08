var fs = require('fs');

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

    var algoritmo = require("./" + algo);
    algoritmo.chave(chave, function(a) {
      var codigo = algoritmo[op](data.toString(), a);

      var saida = algo + "_" + op + ".txt";
      gravaSaida(saida, codigo);
    });
  });
});
