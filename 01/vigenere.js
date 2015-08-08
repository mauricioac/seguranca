function repeat(string, n) {
  var str = "";

  for (var i = 0; i < n; i++) {
    str += string;
  }

  return str;
}
module.exports = {
  cifra: function(string, chave) {
    var newData = "";
    var chaveExtendida = repeat(chave, Math.ceil(string.length / chave.length));

    for (var i = 0; i < string.length; i++) {
      newData += String.fromCharCode((string.charCodeAt(i) + chaveExtendida.charCodeAt(i) + 256) % 256);
    }

    return newData;
  },
  decifra: function(string, chave) {
    var newData = "";
    var chaveExtendida = repeat(chave, Math.ceil(string.length / chave.length));

    for (var i = 0; i < string.length; i++) {
      newData += String.fromCharCode((string.charCodeAt(i) - chaveExtendida.charCodeAt(i) + 256) % 256);
    }

    return newData;
  },
  chave: function(chave, callback) {
    callback(chave);
  }
}
