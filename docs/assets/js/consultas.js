Consultas = {

    urlDefault: "https://putthespoon-api.herokuapp.com/api/1",

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
    },
    
    requestGet: function (funcao, url, arg1=null, arg2=null, arg3=null) {

        $.ajax({
            headers: {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': 'true'
            },
            type: "GET",
            dataType: "json",
            contentType: "application/json; charset=utf-8",
            crossDomain: true,
            url: Consultas.getUrl(url, arg1, arg2, arg3),
            success: function (data) {
                window[funcao](data);
            },
            error: function (e) {
                console.log("Error: ", e);
            }
        });
    },

};