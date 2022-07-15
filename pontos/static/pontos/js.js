function retornajson(data){
    let dados ='<dl class="row">';
    for (const key in data) {
        if (Object.hasOwnProperty.call(data, key)) {
            dados += `<dt class="col-sm-6">${key}</dt>`;
            dados += `<dd class="col-sm-6">-${data[key]}</dd>`;
        }
    }
    dados += "</dl>"
    document.getElementById('main').innerHTML = dados;
}
function retornatext(data){
    let dados = data;
    document.getElementById('main').innerHTML = dados;
}
function requisicaojson(url){  
    fetch(url, {
        method: 'get',
    }).then(result => {
        return result.json()
    }).then(data => {
        retornajson(data);
    })
}
function requisicaotext(url){  
    fetch(url, {
        method: 'get',
    }).then(result => {
        return result.text();
    }).then(data => {
        retornatext(data);
    })
}
function nav_base(indice=0,usuario="Usuário"){
    let nav_list = ["Pontos","Empresas","Funcionários","Registros",usuario];
    let lista_nav = ``;
    let classe_ativa = 'class="col p-1 mt-1 nav-link active text-primary"';
    let classe = 'class="col p-1 m-1 nav-item btn btn-danger"';
    for (let i=0;i<nav_list.length;i++){
        lista_nav += `<li id="${nav_list[i]}" onclick="nav_base(${i})" ${indice===i?classe_ativa:classe}>
        ${nav_list[i]}</li>`;
    }
    document.getElementById('nav').innerHTML = lista_nav;
    switch(indice){
        case 0:
            requisicaotext("pontos");
            window.document.title="Pontos";
            break
        case 1:
            requisicaojson("empresas");
            window.document.title="Empresas";
            break
        case 2:
            requisicaojson("funcionarios");
            window.document.title="Funcionários";
            break
        case 3:
           requisicaojson("registros");
           window.document.title="Registros";
            break
        case 4:
            console.log("indice=>4");
            window.document.title="Usuário";
             break

    }
}