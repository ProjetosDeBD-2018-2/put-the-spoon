# Put The Spoon - Dashboard 
[![version][version-badge]][CHANGELOG] [![license][license-badge]][LICENSE]

### O que está incluso:

Ao clonar ou baixar o este projeto, você o encontrará com a seguinte estrutura:

```
x_lbd_free/
├── assets/
|   ├── css/
|   ├── sass/
|   ├── js/
|   ├── fonts/
|   └── img/
├── consultas/
|   ├── consulta1.html
|   ├── consulta2.html
|   ├── consulta3.html
|   ├── consulta4.html
|   └── consulta5.html
├── CHANGELOG.md
├── LICENSE.md
├── README.md
├── index.html
├── glossario.html
└── quem-somos.html
```

### Como rodar o projeto:

É somente necessario abri o  arquivo `index.html` no navegador.

### Observação:

O projeto no repositório está configurado para utilizar o backend rodando `remoto`, para mudar o endereço para localhost é necessario acessar o arquivo `./assests/js/consultas.js` e na parte:

```
{

    urlDefault: "https://putthespoon-api.herokuapp.com/api/1",

    // urlDefault: "http://localhost:5000/api/1",

    getUrl: function (url, arg1 = null, arg2 = null, arg3 = null){
        var url_complete = Consultas.urlDefault + url;
        if (arg1 != null) {
            url_complete = url_complete + '/' + arg1;
            if (arg2 != null) {
                url_complete = url_complete + '/' + arg2;
                if (arg3 != null) {
                    url_complete = url_complete + '/' + arg3;
                    return url_complete;
                }
                return url_complete;
            }
            return url_complete;
        }
        return url_complete;
    }
```

Descomentar `urlDefault: "http://localhost:5000/api/1"` removendo o `//` e comentar `urlDefault: "https://putthespoon-api.herokuapp.com/api/1"` adicionando `//` no inicio da variavel. 

Para fazer essa alteracao pode ser utilizado qualquer editor de texto plano.

### License

- Initial template Light Bootstrap Dashboard by Creative Tim
- Copyright 2017 Creative Tim (http://www.creative-tim.com)
- Licensed under MIT (https://github.com/creativetimofficial/light-bootstrap-dashboard/blob/master/LICENSE.md)

[CHANGELOG]: ./CHANGELOG.md
[LICENSE]: ./LICENSE.md
[version-badge]: https://img.shields.io/badge/version-1.0.0-blue.svg
[license-badge]: https://img.shields.io/badge/license-MIT-blue.svg
