// https://gist.github.com/femto113/1784503
function transpose(a)
{
  return a[0].map(function (_, c) { return a.map(function (r) { return r[c]; }); });
}

module.exports = {
  cifra: function(string, chave) {
    var matriz = [];
    var linha = -1;
    var i;

    for (i = 0; i < string.length; i++) {
      if (i % chave == 0) {
        matriz.push([]);
        linha++;
      }

      matriz[linha][i % chave] = string[i];
    }

    for (i = i % chave; i < chave; i++) {
      matriz[linha][i] = " ";
    }

    matriz = transpose(matriz);

    var str = "";

    for (var i = 0; i < matriz.length; i++) {
      for (var j = 0; j < matriz[0].length; j++) {
        str += matriz[i][j];
      }
    }

    return str;
  },
  decifra: function(string, chave) {
    var matriz = [];
    var linha = -1;
    var i;

    teto = string.length / chave;

    for (i = 0; i < string.length; i++) {
      if (i % teto == 0) {
        matriz.push([]);
        linha++;
      }

      matriz[linha][i % teto] = string[i];
    }

    var str = "";

    for (var j = 0; j < matriz[0].length; j++) {
      for (var i = 0; i < matriz.length; i++) {
        str += matriz[i][j];
      }
    }

    return str.trim();
  },
  chave: function(chave, callback) {
    callback(parseInt(chave, 10));
  }
}
