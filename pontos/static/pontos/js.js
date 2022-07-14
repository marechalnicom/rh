function registros(url){  
    fetch(url, {
        method: 'get',
    }).then(function(result){
        console.log(result);
        return result.json()
    }).then(function(data){
        let dados ="<dl>";
        for (const key in data) {
            if (Object.hasOwnProperty.call(data, key)) {
                const array = data[key];
                array.forEach(registro => {
                    for (const datas in registro) {
                        if (Object.hasOwnProperty.call(registro, datas)) {
                            console.log(datas,registro[datas]);
                            dados += "<dt>"+datas+"</dt>"
                            dados += "<dd>-"+registro[datas]+"</dd>"
                        }
                    }
                });
            }
        }
        dados += "</dl>"
        document.getElementById('main').innerHTML = dados;
        console.log(dados);
    })
}
function nav_base(indice=0){
    let nav_list = ["Home","Empresas","Funcionários","Registros","Usuário",
        indice,'0 nav-link active text-primary','1 nav-item'];
    let lista_nav = ``;
    for (let i=0;i<5;i++){
        lista_nav += `<li id="${nav_list[i]}" onclick="nav_base(${i})"
        class="col-sm pt-2 m-${indice===i?nav_list[6]:nav_list[7]}">
        ${nav_list[i]}</li>`;
    }
    document.getElementById('nav').innerHTML = lista_nav;
    switch(indice){
        case 0:
            console.log("indice=>0");
            break
        case 1:
           console.log("indice=>1");
           registros("empresas");
            break
        case 2:
            console.log("indice=>2");
            break
        case 3:
           console.log("indice=>3");
           registros("registros");
            break
        case 4:
            console.log("indice=>4");
             break

    }
}