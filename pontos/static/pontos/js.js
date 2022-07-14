function retorna(data){
    let dados ="<dl>";
        for (const key in data) {
            if (Object.hasOwnProperty.call(data, key)) {
                dados += "<dt>"+key+"</dt>"
                dados += "<dd>-"+data[key]+"</dd>"
            }
        }
        dados += "</dl>"
        document.getElementById('main').innerHTML = dados;
}
function requisicao(url){  
    fetch(url, {
        method: 'get',
    }).then(result => {
        return result.json()
    }).then(data => {
        retorna(data);
    })
}
function nav_base(indice=0){
    let nav_list = ["Home","Empresas","Funcionários","Registros","Usuário"];
    let lista_nav = ``;
    let classe_ativa = 'class="col-sm pt-2 m-0 nav-link active text-primary"';
    let classe = 'class="col-sm pt-2 m-1 nav-item"';
    for (let i=0;i<5;i++){
        lista_nav += `<li id="${nav_list[i]}" onclick="nav_base(${i})" ${indice===i?classe_ativa:classe}>
        ${nav_list[i]}</li>`;
    }
    document.getElementById('nav').innerHTML = lista_nav;
    switch(indice){
        case 0:
            console.log("indice=>0");
            break
        case 1:
           requisicao("empresas");
            break
        case 2:
            requisicao("funcionarios");
            break
        case 3:
           requisicao("registros");
            break
        case 4:
            console.log("indice=>4");
             break

    }
}