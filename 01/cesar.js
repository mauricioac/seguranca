module.exports = {
  cifra: function(string, chave) {
    var newData = "";

    for (var i = 0; i < string.length; i++) {
      newData += String.fromCharCode((string.charCodeAt(i) + chave) % 256);
    }

    return newData;
  },
  decifra: function(string, chave) {
    var newData = "";

    for (var i = 0; i < string.length; i++) {
      newData += String.fromCharCode((string.charCodeAt(i) - chave) % 256);
    }

    return newData;
  }
}
