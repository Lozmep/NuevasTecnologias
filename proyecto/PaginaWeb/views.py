from django.shortcuts import render
from django.http import HttpResponse


#CREADO POR: Mauricio Lozano
def PaginaPrincipal(response):
    return HttpResponse('''
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Página Principal</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
            <style>
                *{ margin: 0; padding: 0; box-sizing: border-box; }
                .row {
                    margin-right: auto;
                    margin-left: auto;
                }
                .discount-label {
                    background-color: red;
                    padding:8px; 
                    position:absolute;
                    float:left;
                    margin-top:-120px;
                    margin-left:60px;
                    width:30px;
                    border-radius: 50%;
                    transform: rotate(30deg);
                }
                .discount-label span {
                    color:#ffffff;
                    text-align:center;
                    font-family:"Raleway",Helvetica;
                }
            </style>
            <script src="https://kit.fontawesome.com/638f505c64.js" crossorigin="anonymous"></script>
        </head>
        <body style="background-color: #fef7f7;">
            <div class="row">
                <div class="rounded-3" style="background: rgb(0,0,0);background: linear-gradient(90deg, rgba(0,0,0,1) 0%, rgba(61,0,0,1) 35%);;color:aliceblue;font-size: 1.6rem;">
                <h1 class="text-center  mt-2" style="font-size: 2.5rem;">Nombre Página / Logo</h1>
                <p class="text-center" style="font-size: 1.5rem;">Alguna frase</p>
                <hr style="margin: 0;">
                <nav class="navbar navbar-expand-lg">
                    <div class="container-fluid">
                        <a class="navbar-brand" href="#" style="color: aliceblue;font-size: 2rem;">Logo</a>
                        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                        </button>
                        <div class="collapse navbar-collapse" id="navbarNav">
                            <ul class="navbar-nav">
                                <li class="nav-item">
                                <a class="nav-link" href="Noticias" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Noticias</a>
                                </li>
                                <li class="nav-item">
                                <a class="nav-link" href="Analisis" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Análisis</a>
                                </li>
                                <li class="nav-item">
                                <a class="nav-link" href="Guias" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Guías</a>
                                </li>
                                <li class="nav-item">
                                <a class="nav-link" href="Foro" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Foro</a>
                                </li>
                            </ul>
                        </div>
                    </div>
                </nav>
                </div>
            </div> 
            <div class="row">
                <div class="col-6 mt-2">
                    <div class="container-fluid" style="width: 80%;">            
                        <h2 class="text-center" style="background-color:black;color:aliceblue;">Últimas Noticias</h2>
                        <div id="carouselExampleFade" class="carousel slide carousel-fade mt-3" data-bs-ride="carousel">
                            <div class="carousel-inner">
                                <div class="carousel-item active">
                                    <img src="https://cdn.cloudflare.steamstatic.com/steamcommunity/public/images/clans/41005067/8fa043dc9fcf4cb1fa04aa99ce71cb8aae072c67.png" class="d-block w-100 img-fluid" alt="Elder Ring">
                                    <div class="carousel-caption d-none d-md-block">
                                        <br><h5>Titulo Noticia</h5>
                                        <p>Descripción corta</p>
                                    </div>
                                </div>
                                <div class="carousel-item">
                                    <img src="https://www.cosmocover.com/wp-content/uploads/2022/02/EN_SIFU_Standard_Edition_Key_Art_16x9-scaled.jpg" class="d-block w-100 img-fluid" alt="Sifu">
                                    <div class="carousel-caption d-none d-md-block">
                                        <h5 class="mt-5">Titulo Noticia</h5>
                                        <p>Descripción corta</p> 
                                    </div>
                                </div>
                                <div class="carousel-item">
                                    <img src="https://as01.epimg.net/meristation/imagenes/2021/04/22/analisis/1619092845_591663_1619164855_noticia_normal.jpg" class="d-block w-100 img-fluid" alt="Nier">
                                    <div class="carousel-caption d-none d-md-block">
                                        <br><h5>Titulo Noticia</h5>
                                        <p>Descripción corta</p>
                                    </div>
                                </div>                
                            </div>
                            <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleFade" data-bs-slide="prev">
                            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                            <span class="visually-hidden">Previous</span>
                            </button>
                            <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleFade" data-bs-slide="next">
                            <span class="carousel-control-next-icon" aria-hidden="true"></span>
                            <span class="visually-hidden">Next</span>
                            </button>
                        </div>
                    </div>
                </div>
                <div class="col-6 mt-2">
                    <h2 class="text-center" style="background-color:black;color:aliceblue;">Publicaciones Destacadas</h2>
                    <div class="container-fluid d-flex justify-content-start mt-3">
                        <img src="https://www.enter.co/wp-content/uploads/2017/03/Persona-5-Protagonist-Introduction.jpg" class="img-fluid" style="width: 15%;border-radius: 20px;" alt="Persona 5">                
                        <div class="container-fluid d-flex flex-column">
                            <h6>Titulo Articulo</h6><p>Autor: Nombre Persona</p>
                        </div>
                    </div>
                    <div class="container-fluid d-flex justify-content-start mt-3">
                        <img src="https://as01.epimg.net/meristation/imagenes/2019/12/13/noticias/1576212548_456802_1576212636_noticia_normal.jpg" class="img-fluid" style="width: 15%;border-radius: 20px;" alt="Sekiro">                
                        <div class="container-fluid d-flex flex-column">
                            <h6>Titulo Articulo</h6><p>Autor: Nombre Persona</p>
                        </div>
                    </div>
                    <div class="container-fluid d-flex justify-content-start mt-3">
                        <img src="https://i.blogs.es/e6560e/f4c4882841adfdc7503b5a4d7a496829/1366_2000.jpg" class="img-fluid" style="width: 15%;border-radius: 20px;" alt="Zelda">                
                        <div class="container-fluid d-flex flex-column">
                            <h6>Titulo Articulo</h6><p>Autor: Nombre Persona</p>
                        </div>
                    </div>
                </div>
                <div class="col-12 mt-3">
                    <h2 class="text-center" style="background-color:black;color:aliceblue;">Ofertas Steam</h2>
                    <div class="cards d-flex flex-wrap justify-content-center">
                        <div class="card-container mt-2 ms-3">
                            <div class="container d-flex justify-content-center align-items-center" style="background-color: #008A27;width: 120px;height: 150px;">
                                <div class="discount-label red" style="position: absolute;"><span style="font-size: 0.5rem;"><strong>-50%</strong></span></div> 
                                <img src="https://uvejuegos.com/img/caratulas/60296/pc.jpg" class="img-fluid" style="width: 115px;height: 130px;" alt="Dark Souls">
                            </div>                
                        </div>
                        <div class="card-container mt-2 ms-3">
                            <div class="container d-flex justify-content-center align-items-center" style="background-color: #008A27;width: 120px;height: 150px;">
                                <div class="discount-label red" style="position: absolute;"><span style="font-size: 0.5rem;"><strong>-77%</strong></span></div>    
                                <img src="https://media.redadn.es/imagenes/tomb-raider-pc_153837.jpg" class="img-fluid" style="width: 115px;height: 130px;" alt="Tomb Raider">
                            </div>                
                        </div>
                        <div class="card-container mt-2 ms-3">
                            <div class="container d-flex justify-content-center align-items-center" style="background-color: #008A27;width: 120px;height: 150px;">
                                <div class="discount-label red" style="position: absolute;"><span style="font-size: 0.5rem;"><strong>-33%</strong></span></div> 
                                <img src="https://i.pinimg.com/236x/f0/0f/aa/f00faa9d57c931debbf589a82cb06d6e.jpg" class="img-fluid" style="width: 115px;height: 130px;" alt="Uncharted">
                            </div>                
                        </div>
                        <div class="card-container mt-2 ms-3">
                            <div class="container d-flex justify-content-center align-items-center" style="background-color: #008A27;width: 120px;height: 150px;">
                                <div class="discount-label red" style="position: absolute;"><span style="font-size: 0.5rem;"><strong>-20%</strong></span></div> 
                                <img src="https://i.blogs.es/55a00e/gris/450_1000.jpg" class="img-fluid" style="width: 115px;height: 130px;" alt="Gris">
                            </div>                
                        </div>
                        <div class="card-container mt-2 ms-3">
                            <div class="container d-flex justify-content-center align-items-center" style="background-color: #008A27;width: 120px;height: 150px;">
                                <div class="discount-label red" style="position: absolute;"><span style="font-size: 0.5rem;"><strong>-80%</strong></span></div> 
                                <img src="https://uvejuegos.com/img/caratulas/53456/pc.jpg" class="img-fluid" style="width: 115px;height: 130px;" alt="Mass Effect Andromeda">
                            </div>                
                        </div>
                        <div class="card-container mt-2 ms-3">
                            <div class="container d-flex justify-content-center align-items-center" style="background-color: #008A27;width: 120px;height: 150px;">
                                <div class="discount-label red" style="position: absolute;"><span style="font-size: 0.5rem;"><strong>-10%</strong></span></div> 
                                <img src="https://cdn.tutsplus.com/cdn-cgi/image/width=640/psd/uploads/legacy/psdtutsarticles/linkb_60vgamecovers/19.jpg" class="img-fluid" style="width: 115px;height: 130px;" alt="Half life 2">
                            </div>                
                        </div>
                        <div class="card-container mt-2 ms-3">
                            <div class="container d-flex justify-content-center align-items-center" style="background-color: #008A27;width: 120px;height: 150px;">
                                <div class="discount-label red" style="position: absolute;"><span style="font-size: 0.5rem;"><strong>-60%</strong></span></div> 
                                <img src="https://sm.ign.com/ign_es/screenshot/default/781-2_4na5.jpg" class="img-fluid" style="width: 115px;height: 130px;" alt="Mafia">
                            </div>                
                        </div>
                        <div class="card-container mt-2 ms-3">
                            <div class="container d-flex justify-content-center align-items-center" style="background-color: #008A27;width: 120px;height: 150px;">
                                <div class="discount-label red" style="position: absolute;"><span style="font-size: 0.5rem;"><strong>-70%</strong></span></div> 
                                <img src="https://i.3djuegos.com/juegos/5635/darksiders_ii/fotos/ficha/darksiders_ii-1960314.jpg" class="img-fluid" style="width: 115px;height: 130px;" alt="Darksiders">
                            </div>                
                        </div>
                        <div class="card-container mt-2 ms-3">
                            <div class="container d-flex justify-content-center align-items-center" style="background-color: #008A27;width: 120px;height: 150px;">
                                <div class="discount-label red" style="position: absolute;"><span style="font-size: 0.5rem;"><strong>-35%</strong></span></div> 
                                <img src="https://cl.buscafs.com/www.levelup.com/public/uploads/images/478984_256x320.jpg" class="img-fluid" style="width: 115px;height: 130px;" alt="Hollow Knight">
                            </div>                
                        </div>
                        <div class="card-container mt-2 ms-3">
                            <div class="container d-flex justify-content-center align-items-center" style="background-color: #008A27;width: 120px;height: 150px;">
                                <div class="discount-label red" style="position: absolute;"><span style="font-size: 0.5rem;"><strong>-35%</strong></span></div> 
                                <img src="https://cdn.hobbyconsolas.com/sites/navi.axelspringer.es/public/styles/hc_167x260/public/media/image/2018/01/celeste-portada.jpg?itok=zaHBO9eM" class="img-fluid" style="width: 115px;height: 130px;" alt="Hollow Knight">
                            </div>                
                        </div>
                        <div class="card-container mt-2 ms-3">
                            <div class="container d-flex justify-content-center align-items-center" style="background-color: #008A27;width: 120px;height: 150px;">
                                <div class="discount-label red" style="position: absolute;"><span style="font-size: 0.5rem;"><strong>-35%</strong></span></div> 
                                <img src="https://cdn.hobbyconsolas.com/sites/navi.axelspringer.es/public/styles/1200/public/media/image/2018/01/sfv-arcade-edition-portada.jpg" class="img-fluid" style="width: 115px;height: 130px;" alt="Hollow Knight">
                            </div>                
                        </div>
                        <div class="card-container mt-2 ms-3">
                            <div class="container d-flex justify-content-center align-items-center" style="background-color: #008A27;width: 120px;height: 150px;">
                                <div class="discount-label red" style="position: absolute;"><span style="font-size: 0.5rem;"><strong>-35%</strong></span></div> 
                                <img src="https://cdn.alfabetajuega.com/alfabetajuega/abj_public_files/multimedia/imagenes/201212/28054.cover7.jpg" class="img-fluid" style="width: 115px;height: 130px;" alt="Hollow Knight">
                            </div>                
                        </div>
                    </div>
                </div>
            </div>
            <div class="row mt-4">
                <div class="container-fluid" style="background-color: #191A19;">
                    <footer class="d-flex flex-wrap justify-content-between align-items-center">
                    <div class="col-md-4 d-flex align-items-center ms-5">
                        <a href="/" class="mb-3 me-2 mb-md-0 text-muted text-decoration-none lh-1">
                            <i style="color: aliceblue; font-size: 2.5rem;" class="fa-brands fa-bootstrap"></i>
                        </a>
                        <span style="font-size: 1.5rem;" class="mb-3 mb-md-0 text-muted"><p style="color: aliceblue;" class="mt-3">&copy; 2022 Nombre Página, Inc</p></span>
                    </div>      
                    <ul class="nav col-md-4 justify-content-end list-unstyled d-flex me-5">
                        <li class="ms-3"><a class="text-muted" href="#"><i style="color: aliceblue; font-size: 2.5rem;" class="fa-brands fa-twitter"></i></a></li>
                        <li class="ms-3"><a class="text-muted" href="#"><i style="color: aliceblue; font-size: 2.5rem;" class="fa-brands fa-instagram"></i></a></li>
                        <li class="ms-3"><a class="text-muted" href="#"><i style="color: aliceblue; font-size: 2.5rem;" class="fa-brands fa-facebook-f"></i></a></li>
                    </ul>
                    </footer>
                </div>
            </div>
        </body>
        </html>
    ''')

#########################################################################################
#########################################################################################

#CREADO POR: Victor Rios
def Noticias(response):
    return HttpResponse('''
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Noticias</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
        <style>
            *{ margin: 0; padding: 0; box-sizing: border-box; }
            .row {
                margin-right: auto;
                margin-left: auto;
            }
            #jumbo{
                margin-bottom: 0; 
                color: white;
                background-image: url(https://www.nitro-pc.es/blog/wp-content/uploads/2020/08/Portada-juegos-baratos.png);
                background-color: #cccccc;
                background-position: center;
                background-repeat: no-repeat;
                background-size: cover;
                position: relative;
                height: 100%;
        
            }
            a{
                text-decoration: none!important;
                color: black;
            }
            #frase{
                background-color: rgba(61,0,0,0.5);
            }
            #upi{
                color: #E04646;
            }
            #upi:hover{
                color: white!important;
            }
            .active{
                color: #E04646!important
            }
            .nav-link:hover,.bi:hover{
                color: #E04646!important
            }
            .abs-center {
                display: flex;
                align-items: center;
                justify-content: center;
            }
            #card:hover{
                box-shadow: 5px 0px 40px rgba(224, 70, 70, 0.596);
                -webkit-transform: scale(1.1);
                transform: scale(1.1);
                color: #212529!important; 
            }
            
        </style>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.9.1/font/bootstrap-icons.css">
        
    </head>
    <body style="background-color: #fef7f7;">
        <div class="row">
            <div class="rounded-3" style="background: rgb(0,0,0);background: linear-gradient(90deg, rgba(0,0,0,1) 0%, rgba(61,0,0,1) 35%);;color:aliceblue;font-size: 1.6rem;">
            <h1 class="text-center  mt-2" style="font-size: 2.5rem;">Nombre Página / Logo</h1>
            <p class="text-center" style="font-size: 1.5rem;">Alguna frase</p>
            <hr style="margin: 0;">
            <nav class="navbar navbar-expand-lg">
                <div class="container-fluid">
                    <a class="navbar-brand" href="../" style="color: aliceblue;font-size: 2rem;">Logo</a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarNav">
                        <ul class="navbar-nav">
                            <li class="nav-item">
                            <a class="nav-link" href="#" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Noticias</a>
                            </li>
                            <li class="nav-item">
                            <a class="nav-link" href="../Analisis" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Análisis</a>
                            </li>
                            <li class="nav-item">
                            <a class="nav-link" href="../Guias" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Guías</a>
                            </li>
                            <li class="nav-item">
                            <a class="nav-link" href="../Foro" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Foro</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
            </div>
        </div> 
        <br><br>
        <section>        
            <div class="row">
                <div class="col ">
                    <div class="row text-center"  style="background-color: black;">
                        <strong><h2 style="color:aliceblue;">NUESTRO CONTENIDO</h2></strong>
                    </div>
                    <br><br><br>
                    <div class="row">
                        <p style="color: black;text-align:justify;">Aquí encontrarás todas las noticias y las últimas novedades en videojuegos. Recopilamos cada día y minuto a minuto toda la actualidad del mundo de los videojuegos y sus diferentes plataformas para que siempre estés al corriente de la última actualización o contenido relacionado con tus títulos preferidos, de las fechas de lanzamiento de los juegos más esperados, los anuncios más importantes, reportajes, entrevistas, declaraciones, nuevas imágenes o tráileres y todas las curiosidades del mundillo para mantenerte informado y a la vez entretenido.</p>
                    </div>
                
                </div>
                <div class="col">
                    <div class="row text-center"  style="background-color: black;">
                        <strong><h2 style="color:aliceblue;">ÚLTIMO VIDEO</h2></strong>
                    </div><br><br>
                    <div class="ratio ratio-16x9" >
                        <iframe src="https://www.youtube.com/embed/ezKQ-FE4UEQ" title="YouTube video" allowfullscreen></iframe>
                    </div>
                </div>
            </div>
            <br><br>
        </section>
        <section style="background-color: #FEF7F7;">
            <br>
            <div class="row text-center"  style="background-color: black;">
                <strong><h2 style="color:aliceblue;">ÚLTIMAS NOTICIAS</h2></strong>
            </div>
        </section>
        <br>
        <section style="background-color: #FEF7F7;">
            <br><br>
            <div class="row ">
                <div class="col abs-center">
                    <a href="https://vandal.elespanol.com/noticia/1350755903/kena-bridge-of-spirits-llega-a-steam-en-septiembre-con-nuevos-modos-y-opciones/">
                        <div class="card mb-3" id="card" style="max-width: 540px;">
                            <div class="row g-0">
                            <div class="col-md-4">
                                <img src="https://3y3seo1md7o8303qa48ddzzb-wpengine.netdna-ssl.com/wp-content/uploads/2022/06/gamer.png" class="img-fluid rounded-start" alt="...">
                            </div>
                            <div class="col-md-8">
                                <div class="card-body">
                                <h5 class="card-title">Titulo</h5>
                                <p class="card-text">Lorem ipsum dolor sit amet consectetur adipisicing elit. Vel maiores ipsa perspiciatis labore? Ea delectus est suscipit fugit nostrum sapiente quas exercitationem? Accusantium minima qui fugiat ipsam, pariatur quis blanditiis.</p>
                                <p class="card-text">
                                    <small class="text-muted"><i class="bi bi-clock-fill"></i> Last updated 3 mins ago</small>
                                    <small class="text-muted"><i class="bi bi-person-fill"></i> Kevin Mier</small>
                                </p>
                                
                                </div>
                            </div>
                            </div>
                        </div>
                    </a>
                </div>
                <div class="col abs-center">
                    <a href="https://vandal.elespanol.com/noticia/1350755903/kena-bridge-of-spirits-llega-a-steam-en-septiembre-con-nuevos-modos-y-opciones/">
                        <div class="card mb-3" id="card" style="max-width: 540px;">
                            <div class="row g-0">
                            <div class="col-md-4">
                                <img src="https://3y3seo1md7o8303qa48ddzzb-wpengine.netdna-ssl.com/wp-content/uploads/2022/06/gamer.png" class="img-fluid rounded-start" alt="...">
                            </div>
                            <div class="col-md-8">
                                <div class="card-body">
                                <h5 class="card-title">Titulo</h5>
                                <p class="card-text">Lorem ipsum dolor sit amet consectetur adipisicing elit. Vel maiores ipsa perspiciatis labore? Ea delectus est suscipit fugit nostrum sapiente quas exercitationem? Accusantium minima qui fugiat ipsam, pariatur quis blanditiis.</p>
                                <p class="card-text">
                                    <small class="text-muted"><i class="bi bi-clock-fill"></i> Last updated 3 mins ago</small>
                                    <small class="text-muted"><i class="bi bi-person-fill"></i> Kevin Mier</small>
                                </p>
                                
                                </div>
                            </div>
                            </div>
                        </div>
                    </a>
                </div>
            </div>
            <br>
            <div class="row ">
                <div class="col abs-center">
                    <a href="https://vandal.elespanol.com/noticia/1350755903/kena-bridge-of-spirits-llega-a-steam-en-septiembre-con-nuevos-modos-y-opciones/">
                        <div class="card mb-3" id="card" style="max-width: 540px;">
                            <div class="row g-0">
                            <div class="col-md-4">
                                <img src="https://3y3seo1md7o8303qa48ddzzb-wpengine.netdna-ssl.com/wp-content/uploads/2022/06/gamer.png" class="img-fluid rounded-start" alt="...">
                            </div>
                            <div class="col-md-8">
                                <div class="card-body">
                                <h5 class="card-title">Titulo</h5>
                                <p class="card-text">Lorem ipsum dolor sit amet consectetur adipisicing elit. Vel maiores ipsa perspiciatis labore? Ea delectus est suscipit fugit nostrum sapiente quas exercitationem? Accusantium minima qui fugiat ipsam, pariatur quis blanditiis.</p>
                                <p class="card-text">
                                    <small class="text-muted"><i class="bi bi-clock-fill"></i> Last updated 3 mins ago</small>
                                    <small class="text-muted"><i class="bi bi-person-fill"></i> Kevin Mier</small>
                                </p>
                                
                                </div>
                            </div>
                            </div>
                        </div>
                    </a>
                </div>
                <div class="col abs-center">
                    <a href="https://vandal.elespanol.com/noticia/1350755903/kena-bridge-of-spirits-llega-a-steam-en-septiembre-con-nuevos-modos-y-opciones/">
                        <div class="card mb-3" id="card" style="max-width: 540px;">
                            <div class="row g-0">
                            <div class="col-md-4">
                                <img src="https://3y3seo1md7o8303qa48ddzzb-wpengine.netdna-ssl.com/wp-content/uploads/2022/06/gamer.png" class="img-fluid rounded-start" alt="...">
                            </div>
                            <div class="col-md-8">
                                <div class="card-body">
                                <h5 class="card-title">Titulo</h5>
                                <p class="card-text">Lorem ipsum dolor sit amet consectetur adipisicing elit. Vel maiores ipsa perspiciatis labore? Ea delectus est suscipit fugit nostrum sapiente quas exercitationem? Accusantium minima qui fugiat ipsam, pariatur quis blanditiis.</p>
                                <p class="card-text">
                                    <small class="text-muted"><i class="bi bi-clock-fill"></i> Last updated 3 mins ago</small>
                                    <small class="text-muted"><i class="bi bi-person-fill"></i> Kevin Mier</small>
                                </p>
                                
                                </div>
                            </div>
                            </div>
                        </div>
                    </a>
                </div>
            </div>
        </section>
        <div class="row mt-4">
            <div class="container-fluid" style="background-color: #191A19;">
                <footer class="d-flex flex-wrap justify-content-between align-items-center">
                <div class="col-md-4 d-flex align-items-center ms-5">
                    <a href="/" class="mb-3 me-2 mb-md-0 text-muted text-decoration-none lh-1">
                        <i style="color: aliceblue; font-size: 2.5rem;" class="fa-brands fa-bootstrap"></i>
                    </a>
                    <span style="font-size: 1.5rem;" class="mb-3 mb-md-0 text-muted"><p style="color: aliceblue;" class="mt-3">&copy; 2022 Nombre Página, Inc</p></span>
                </div>      
                <ul class="nav col-md-4 justify-content-end list-unstyled d-flex me-5">
                    <li class="ms-3"><a class="text-muted" href="#"><i style="color: aliceblue; font-size: 2.5rem;" class="fa-brands fa-twitter"></i></a></li>
                    <li class="ms-3"><a class="text-muted" href="#"><i style="color: aliceblue; font-size: 2.5rem;" class="fa-brands fa-instagram"></i></a></li>
                    <li class="ms-3"><a class="text-muted" href="#"><i style="color: aliceblue; font-size: 2.5rem;" class="fa-brands fa-facebook-f"></i></a></li>
                </ul>
                </footer>
            </div>
        </div>
    </body>
    </html>
    ''')

#########################################################################################
#########################################################################################

#CREADO POR: Juan Camilo Cano
def Foro(response):
    return HttpResponse('''
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Foro</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
            <style>
                *{ margin: 0; padding: 0; box-sizing: border-box; }
                .row {
                    margin-right: auto;
                    margin-left: auto;
                }
            </style>
            <script src="https://kit.fontawesome.com/638f505c64.js" crossorigin="anonymous"></script>
        </head>
        <body style=" background: url(https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ02qYYeqeXEnbgAN_I4-AaDzDx0btqxvzW7g&usqp=CAU);">
            <div class="row">
                <div class="rounded-3" style="background: rgb(0,0,0);background: linear-gradient(90deg, rgba(0,0,0,1) 0%, rgba(61,0,0,1) 35%);;color:aliceblue;font-size: 1.6rem;">
                <h1 class="text-center  mt-2" style="font-size: 2.5rem;">Nombre Página / Logo</h1>
                <p class="text-center" style="font-size: 1.5rem;">Alguna frase</p>
                <hr style="margin: 0;">
                <nav class="navbar navbar-expand-lg">
                    <div class="container-fluid">
                        <a class="navbar-brand" href="../" style="color: aliceblue;font-size: 2rem;">Logo</a>
                        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                        </button>
                        <div class="collapse navbar-collapse" id="navbarNav">
                            <ul class="navbar-nav">
                                <li class="nav-item">
                                <a class="nav-link" href="../Noticias" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Noticias</a>
                                </li>
                                <li class="nav-item">
                                <a class="nav-link" href="../Analisis" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Análisis</a>
                                </li>
                                <li class="nav-item">
                                <a class="nav-link" href="../Guias" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Guías</a>
                                </li>
                                <li class="nav-item">
                                <a class="nav-link active" href="#" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Foro</a>
                                </li>
                            </ul>
                        </div>
                    </div>
                </nav>
                </div>
            </div> 
        
            <div class="col-10  row d-flex justify-content-center"style="background-color: #fef7f7;">
                <div class="row">
                    <div class="col-6 mt-2">
                        <h4 class="text-right"style="background-color: #000000;border-radius: 20px;color: aliceblue;"><p class="titxex1" style="margin-left: 5%">VIDEOJUEGOS</p></h4>
 
                    </div>
                    <div class="col-6 mt-2" >
                        <h4 class="text-right" style="background-color: #000000;border-radius: 20px;color: aliceblue;"><p class="titxex1" style="margin-left: 5%">Últimos Posts</p></h4>
                    </div>
                </div>
                <div class="row">
                    <div class="col-6 mt-2">
                        <div class="container-fluid d-flex justify-content-start mt-3">
                            <img src="https://cdn-icons-png.flaticon.com/128/8286/8286658.png" class="img-fluid" style="width: 15%;border-radius: 20px;" alt="Sekiro">                
                            <div class="container-fluid d-flex flex-column">
                                 <h6><a href="/" style="color: #000000; text-decoration: none;" >Videojuegos en general</a></h6><p>Temas sobre juegos en general. Lanzamientos, actualidad, gustos, preguntas...</p>
                            </div>
                        </div>  
                    </div>
                    <div class="col-6 mt-2">
                        <div class="container-fluid d-flex justify-content-start mt-3">
                                                
                            <div class="container-fluid d-flex flex-column">
                                <h6><a href="/" style="color: #000000; text-decoration: none;" >9 minutos - Cyber_Turbo_R</a></h6>
                                <p>[Post oficial V.4] CAPTURAS DE JUEGOS</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-6 mt-2">
                        <div class="container-fluid d-flex justify-content-start mt-3">
                            <img src="https://cdn-icons-png.flaticon.com/128/189/189533.png" class="img-fluid" style="width: 15%;border-radius: 20px;" alt="Sekiro">                
                            <div class="container-fluid d-flex flex-column">
                                <h6> <a href="/" style="color: #000000; text-decoration: none;" >Videojuegos específicos</a></h6><p>Encuentra el foro de tu juego preferido y relaciónate con su comunidad.</p>
                            </div>
                        </div>  
                    </div>
                    <div class="col-6 mt-2">
                        <div class="container-fluid d-flex justify-content-start mt-3">
                                                
                            <div class="container-fluid d-flex flex-column">
                                <h6><a href="/" style="color: #000000; text-decoration: none;" >un momento - edurance</a></h6><p> Noticia: PlayStation se enfrenta a una demanda millonaria por una presunta 'estafa' al consumidor </p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-6 mt-2">
                        <div class="container-fluid d-flex justify-content-start mt-3">
                            <img src="https://cdn-icons-png.flaticon.com/128/2005/2005003.png" class="img-fluid" style="width: 15%;border-radius: 2px;" alt="Sekiro">                
                            <div class="container-fluid d-flex flex-column">
                                <h6><a href="/" style="color: #000000; text-decoration: none;" >Noticias y actualidad</a></h6><p>Tribuna abierta para comentar las noticias del mundo del videojuego.</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-6 mt-2">
                        <div class="container-fluid d-flex justify-content-start mt-3">
                            <div class="container-fluid d-flex flex-column">
                                <h6><a href="/" style="color: #000000; text-decoration: none;" >13 minutos - LordDagak</a></h6><p>● Sonic  Post oficial ●  Sonic Frontiers estas Navidades</p>
                            </div>               
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-6 mt-2">
                        <h4 class="text-right"style="background-color: #000000;border-radius: 20px;color: aliceblue;"><p class="titxex1" style="margin-left: 5%">MÁS QUE VIDEOJUEGOS</p></h4>
 
                    </div>
                    <div class="col-6 mt-2" >
                        <h4 class="text-right" style="background-color: #000000;border-radius: 20px;color: aliceblue;"><p class="titxex1" style="margin-left: 5%">Últimos Posts</p></h4>
                    </div>
                </div>
                <div class="row">
                    <div class="col-6 mt-2">
                        <div class="container-fluid d-flex justify-content-start mt-3">
                            <img src="https://cdn-icons-png.flaticon.com/128/7509/7509773.png" class="img-fluid" style="width: 15%;border-radius: 2px;" alt="Sekiro">                
                            <div class="container-fluid d-flex flex-column">
                                <h6><a href="/" style="color: #000000; text-decoration: none;" >Off Topic y humor</a></h6><p>Hablemos de todo menos de juegos o temas de otros foros.</p>
                            </div>
                        </div>  
                    </div>
                    <div class="col-6 mt-2">
                        <div class="container-fluid d-flex justify-content-start mt-3">
                            <div class="container-fluid d-flex flex-column">
                                <h6><a href="/" style="color: #000000; text-decoration: none;" >4 horas - Jocs_204</a></h6><p> GRAN TURISMO 7  Encuentra tu trazada</p>
                            </div>                  
 
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-6 mt-2">
                        <div class="container-fluid d-flex justify-content-start mt-3">
                            <img src="https://cdn-icons-png.flaticon.com/128/3959/3959335.png" class="img-fluid" style="width: 15%;border-radius: 2px;" alt="Sekiro">                
                            <div class="container-fluid d-flex flex-column">
                                <h6><a href="/" style="color: #000000; text-decoration: none;" >Desarrollo de videojuegos</a></h6><p>Comparte proyectos y conocimientos.</p>
                            </div>
                        </div>  
                    </div>
                    <div class="col-6 mt-2">
                        <div class="container-fluid d-flex justify-content-start mt-3">
                            <div class="container-fluid d-flex flex-column">
                                <h6><a href="/" style="color: #000000; text-decoration: none;" >13/06/2022 17:03 - Alendi93</a></h6><p>Discord para aprender Unity y desarrollo de juegos en general [Proyecto serio]</p>
                            </div>                  
 
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-6 mt-2">
                        <h4 class="text-right"style="background-color: #000000;border-radius: 20px;color: aliceblue;"><p class="titxex1" style="margin-left: 5%">SISTEMAS</p></h4>
 
                    </div>
                    <div class="col-6 mt-2" >
                        <h4 class="text-right" style="background-color: #000000;border-radius: 20px;color: aliceblue;"><p class="titxex1" style="margin-left: 5%">Últimos Posts</p></h4>
                    </div>
                </div>
                <div class="row">
                    <div class="col-6 mt-2">
                        <div class="container-fluid d-flex justify-content-start mt-3">
                            <img src="https://cdn-icons-png.flaticon.com/128/2331/2331858.png" class="img-fluid" style="width: 15%;border-radius: 40px;" alt="Sekiro">                
                            <div class="container-fluid d-flex flex-column">
                                <h6><a href="/" style="color: #000000; text-decoration: none;" >	PC / Hardware y presupuestos</a></h6><p>Jugadores de PC, Steam, juegos digitales y expertos en configurar equipos y presupuestos.</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-6 mt-2">
                        <div class="container-fluid d-flex justify-content-start mt-3">
                            <div class="container-fluid d-flex flex-column">
                                <h6><a href="/" style="color: #000000; text-decoration: none;" >19/08/2022 10:39 - Guthwulf</a></h6><p>Monster boy and the cursed kingdom: posible bug</p>
                            </div>             
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-6 mt-2">
                        <div class="container-fluid d-flex justify-content-start mt-3">
                            <img src="https://cdn-icons-png.flaticon.com/128/1724/1724566.png" class="img-fluid" style="width: 15%;border-radius: 2px;" alt="Sekiro">                
                            <div class="container-fluid d-flex flex-column">
                                <h6><a href="/" style="color: #000000; text-decoration: none;" >	PlayStation 5 / PlayStation 4 / PlayStation 3</a></h6><p>Videojuegos, PSN, PSPlus, PlayStation VR y más para los seguidores de consolas Sony</p>
                            </div>
                        </div>  
                    </div>
                    <div class="col-6 mt-2">
                        <div class="container-fluid d-flex justify-content-start mt-3">
                            <div class="container-fluid d-flex flex-column">
                                <h6><a href="/" style="color: #000000; text-decoration: none;" >45 minutos - Safenix</a></h6><p>[Xenohilo Oficial] Saga Xenoblade Chronicles: Monolith does what Retrodont</p>
                            </div>                 
 
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-6 mt-2">
                        <div class="container-fluid d-flex justify-content-start mt-3">
                            <img src="https://cdn-icons-png.flaticon.com/128/588/588298.png" style="width: 15%;border-radius: 20px;" alt="Sekiro">                
                            <div class="container-fluid d-flex flex-column">
                                <h6><a href="/" style="color: #000000; text-decoration: none;" > Xbox Series X / Xbox One / Xbox 360</a></h6><p>Juegos, Xbox Live, Arcade, retrocompatibilidad y todo sobre las consolas Xbox de Microsoft.</p>
                            </div>
                        </div>  
                    </div>
                    <div class="col-6 mt-2">
                        <div class="container-fluid d-flex justify-content-start mt-3">
                            <div class="container-fluid d-flex flex-column">
                                <h6><a href="/" style="color: #000000; text-decoration: none;" >21/06/2021 16:51 - Xilos</a></h6><p>P.O THE LEGEND OF SAGA [Every game has a story, Only one is a legend]b</p>
                            </div>                 
 
                        </div>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="container-fluid" style="background-color: #191A19;">
                    <footer class="d-flex flex-wrap justify-content-between align-items-center">
                    <div class="col-md-4 d-flex align-items-center ms-5">
                        <a href="/" class="mb-3 me-2 mb-md-0 text-muted text-decoration-none lh-1">
                            <i style="color: aliceblue; font-size: 2.5rem;" class="fa-brands fa-bootstrap"></i>
                         </a>
                        <span style="font-size: 1.5rem;" class="mb-3 mb-md-0 text-muted"><p style="color: aliceblue;" class="mt-3">&copy; 2022 Nombre Página, Inc</p></span>
                    </div>      
                        <ul class="nav col-md-4 justify-content-end list-unstyled d-flex me-5">
                            <li class="ms-3"><a class="text-muted" href="#"><i style="color: aliceblue; font-size: 2.5rem;" class="fa-brands fa-twitter"></i></a></li>
                            <li class="ms-3"><a class="text-muted" href="#"><i style="color: aliceblue; font-size: 2.5rem;" class="fa-brands fa-instagram"></i></a></li>
                            <li class="ms-3"><a class="text-muted" href="#"><i style="color: aliceblue; font-size: 2.5rem;" class="fa-brands fa-facebook-f"></i></a></li>
                        </ul>
                        </footer>
                    </div>
                </div>
            </div>
        </body>
        </html>
    ''')

#########################################################################################
#########################################################################################

#CREADO POR: Estiven Zapata
def GuiaGOW(response):
    return HttpResponse('''
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Guías</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
            <style>
                *{ margin: 0; padding: 0; box-sizing: border-box; }
                .row {
                    margin-right: auto;
                    margin-left: auto;
                }
            </style>
        </head>
        <body>
            <div class="row">
                <div class="rounded-3" style="background: rgb(0,0,0);background: linear-gradient(90deg, rgba(0,0,0,1) 0%, rgba(61,0,0,1) 35%);;color:aliceblue;font-size: 1.6rem;">
                <h1 class="text-center  mt-2" style="font-size: 2.5rem;">Nombre Página / Logo</h1>
                <p class="text-center" style="font-size: 1.5rem;">Alguna frase</p>
                <hr style="margin: 0;">
                <nav class="navbar navbar-expand-lg">
                    <div class="container-fluid">
                        <a class="navbar-brand" href="../" style="color: aliceblue;font-size: 2rem;">Logo</a>
                        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                        </button>
                        <div class="collapse navbar-collapse" id="navbarNav">
                            <ul class="navbar-nav">
                                <li class="nav-item">
                                <a class="nav-link" href="../Noticias" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Noticias</a>
                                </li>
                                <li class="nav-item">
                                <a class="nav-link" href="../Analisis" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Análisis</a>
                                </li>
                                <li class="nav-item">
                                <a class="nav-link" href="#" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Guías</a>
                                </li>
                                <li class="nav-item">
                                <a class="nav-link active" href="../Foro" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Foro</a>
                                </li>
                            </ul>
                        </div>
                    </div>
                </nav>
                </div>
            </div> 
            <div class="row d-flex justify-content-center">
                <div class="container-fluid w-75">
                    <div>
                        <h2 class="mt-5 text-center" style="background-color:black;color:aliceblue;">Guía God of War (PC, PS4 y PS5): Trucos, consejos y secretos</h2>
                        <h5 class="mt-3 text-center">Enseña a Kratos a ser padre y a Atreus a ser un dios con la guía más completa de God of War en español.</h5>
                    </div>
                    <div class="mt-3 text-center">
                        <img style="width:70%" src="https://media.vandal.net/m/3-2020/20203218232519_1.jpg" alt="" srcset="">
                    </div>
                    <div class="mt-3">
                        <p style="text-align:justify;">
                            Bienvenidos a la guía más completa de God of War para PS4, PC y PS5. Descubre todos los secretos del juego, complétalo al 100%, consigue todos los trofeos y descúbrelo todo sobre la nueva aventura del dios de la guerra. Como es sabido, Kratos acabó con todo aquello que se interponía en su camino en la antigua Grecia. Sin embargo, ahora, cansado y muy cambiado, vive en los lejanos reinos del norte acompañado de su hijo Atreus. No te dejes nada en God of War PS4 con nuestra guía completa del juego.
                        </p>
                    </div>
                    <div>
                        <h4>Preguntas frecuentes</h4>
                        <p>
                            <ul> <li style="text-align:justify;"> <b>Cómo mejorar las armaduras:</b> Tendrás que esperar a haber avanzado lo suficiente en la historia para desbloquear la tienda. Puedes mejorar tu equipo en cualquiera de las tiendas del juego.</li>
                            </ul>
                            <ul> <li style="text-align:justify;"> <b>Cómo conseguir los materiales para mejorar las armas:</b> Se trata de materiales que el juego nos da automáticamente al derrotar a los jefes. Para la última mejora de las armas principales debes completar los Reinos opcionales.</li>
                            </ul>
                            <ul> <li style="text-align:justify;"> <b>Cómo conseguir mejores armaduras:</b> Las mejores armaduras se consiguen en Niflheim. En los cofres el equipo es la mayoría de veces aleatorio.</li>
                            </ul>
                            <ul> <li style="text-align:justify;"> <b>Cómo conseguir XP y Plata rápidamente;</b> No hay un sistema rápido, el juego está perfectamente equilibrado en este sentido.</li>
                            </ul>
                            <ul> <li style="text-align:justify;"> <b>¿Hace falta haber jugado a los God of War anteriores para entender la historia?</b> No. Siempre que sepas quién es Kratos y a quiénes mató en Grecia, podrás comprender la historia perfectamente.</li>
                            </ul>
                        </p>
                    </div>
                    <div>
                        <h4>Historia</h4>
                        <p style="text-align:justify;">
                            Te contamos cómo superar todas las misiones de historia de God of War, sin spoilers e indicando una buena parte de los coleccionables que encontrarás en tu camino. Si quieres exprimir tu partida al máximo, no te pierdas nuestra guía completa de la historia de God of War.
                        </p>
                    </div>
                    <div>
                        <h4>Favores</h4>
                        <p style="text-align:justify;">
                            God of War nos ofrece unas cuantas misiones secundarias, que en este caso llevan el nombre de Favores. Desde las criaturas más pequeñas hasta los monstruos más grandes, todos tienen algo que pedirte y nosotros te contamos cómo cumplir con todo. Todos los favores.
                        </p>
                    </div>
                    <div>
                        <h4>Valquirias</h4>
                        <p style="text-align:justify;">
                            Las valquirias están de nuevo sobre la tierra. Sin embargo, parece que no lo están precisamente por voluntad propia. Kratos tendrá que enfrentarse a ellas y averiguar qué ha sucedido si quiere arreglar esta situación. Derrotar a todas las valquirias no será fácil, pero nosotros te ayudaremos a salir con vida de los enfrentamientos.
                        </p>
                    </div>
                    <div>
                        <h4>Mapas del tesoro</h4>
                        <p style="text-align:justify;">
                            Un sitio tan antiguo como Midgard no puede tener todo a simple vista. Repartidas por las distintas regiones del Reino de los hombres, encontrarás una serie de ubicaciones que tienen un tesoro oculto. Estos tesoros contienen Recursos especiales, enfocados a poder mejorar nuestros accesorios y, cómo no, conseguir una buena cantidad de Plata.
                            <br><br>
                            No vayas demasiado rápido, porque tendrás que encontrar los mapas para poder coger los tesoros. Lo primero es fácil, para lo segundo puede que tengas problemas, ya que sólo te dan una imagen y una pista de dónde buscar.
                        </p>
                    </div>
                    <div>
                        <h4>Cámaras Ocultas de Odín</h4>
                        <p style="text-align:justify;">
                            El padre de los dioses del norte tiene una serie de escondrijos para sus tesoros repartidos por los Reinos. ¿Qué es lo que realmente ha ocultado en estos lugares y por qué? Sólo hay una manera de averiguarlo: abriendo las Cámaras. Todas las cámaras ocultas de Odín.
                        </p>
                    </div>                    
                </div>
            </div>
        </body>
        </html>
    ''')

#########################################################################################
#########################################################################################

#CREADO POR: Andrés Murillo
def GuiaFreeFire(response):
    return HttpResponse('''
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Guías</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
            <style>
                *{ margin: 0; padding: 0; box-sizing: border-box; }
                .row {
                    margin-right: auto;
                    margin-left: auto;
                }
            </style>
        </head>
        <body>
            <div class="row">
                <div class="rounded-3" style="background: rgb(0,0,0);background: linear-gradient(90deg, rgba(0,0,0,1) 0%, rgba(61,0,0,1) 35%);;color:aliceblue;font-size: 1.6rem;">
                <h1 class="text-center  mt-2" style="font-size: 2.5rem;">Nombre Página / Logo</h1>
                <p class="text-center" style="font-size: 1.5rem;">Alguna frase</p>
                <hr style="margin: 0;">
                <nav class="navbar navbar-expand-lg">
                    <div class="container-fluid">
                        <a class="navbar-brand" href="../" style="color: aliceblue;font-size: 2rem;">Logo</a>
                        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                        </button>
                        <div class="collapse navbar-collapse" id="navbarNav">
                            <ul class="navbar-nav">
                                <li class="nav-item">
                                <a class="nav-link" href="../Noticias" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Noticias</a>
                                </li>
                                <li class="nav-item">
                                <a class="nav-link" href="#" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Análisis</a>
                                </li>
                                <li class="nav-item">
                                <a class="nav-link" href="../Guias" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Guías</a>
                                </li>
                                <li class="nav-item">
                                <a class="nav-link active" href="../Foro" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Foro</a>
                                </li>
                            </ul>
                        </div>
                    </div>
                </nav>
                </div>
            </div> 
            <div class="row d-flex justify-content-center">
                <div class="container-fluid w-75">
                    <div>
                        <h2 class="mt-3 text-center" style="background-color:black;color:aliceblue;">Guía Free Fire, trucos, consejos y secretos</h2>
                        <p class="mt-3">En nuestra completa guía de Free Fire, el popular juego de móviles, te enseñamos los mejores consejos para sobrevivir y ganar en sus intensas y divertidas partidas Battle Royale.</p>
                    </div>
                    <div class="d-flex justify-content-center">
                        <iframe class="mt-3" width="50%" height="380" src="https://www.youtube.com/embed/CgqrHG_3i9g" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                    </div>
                    <div class="mt-3">
                        <p style="text-align:justify;">
                            Bienvenidos a nuestra guía completa de Free Fire, uno de los juegos móviles que más descargas acumulan en el mercado, tanto en dispositivos Android como en iOS de Apple. Garena nos brinda una experiencia de acción en tercera persona al más puro estilo Battle Royale en la que debemos caer en una isla con 50 jugadores y sobrevivir hasta el final... solo si somos capaces. Para ayudaros a brillar en el campo de batalla os traemos en nuestra guía un montón de consejos, trucos y recomendaciones de todo tipo. Aquí podréis encontrar información acerca del arsenal del juego, cómo conseguir diamantes, desbloquear contenidos y mucho más. ¡Rompan filas, soldados!
                        </p>
                    </div>             
                </div>
            </div>
        </body>
        </html>
    ''')


##################################################################################################################################################
##################################################################################################################################################

#CREADO POR: Maria Paulina Otálvaro y Sergio Andrés Restrepo
def Analisis(response):
    return HttpResponse('''
    <html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ANÁLISIS</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
    <style>
        *{ margin: 0; padding: 0; box-sizing: border-box; }
        .row {
            margin-right: auto;
            margin-left: auto;
        }
        
.carousel-caption.d-none.d-md-block {
display: block!important;
margin-bottom: -7%;
}
img.d-block.w-100.img-fluid:hover {
    filter: sepia(60%);
    transition-duration: 2s, 3s, 2s, 3s;
}
div#carouselExampleFade {
    margin-top: 8rem!important;
}
*{ margin: 0; padding: 0; box-sizing: border-box;}
 h2.text-center {
    margin-top: -53.8px;
    margin-bottom: 5%;
}
h3.text-titulo2 {
    font-size: 38px;
    text-align: center;
}
.row {
margin-right: auto;
margin-left: auto;
}
.row-seccion-analisis {
background: wheat;
border: 0;
margin-left: 13vw;
margin-right: 14vw;
margin-top: 10%;
}
.col-12-sec1 {
flex: 0 0 auto;
width: 100%;
height: 50%;
}
p.textoEnlace {
    margin-left: -12%;
    margin-bottom: -11%;
}
p.texto1analisis {
    margin-top: 89px !important;
    margin-bottom: -5rem !important;
    margin-left: -8% !important;
}
                
.tarjeta{
background: black;
display:flex;
flex-direction:column;
justify-content:space-between;
width:420px;
border: 1px solid rgb(32, 15, 15);
box-shadow: 2px 2px 8px 4px #a03131d1;
border-radius:15px;
font-family: sans-serif;
margin-left: 3%;
}
.tarjeta-2{
    background: black;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    width: 420px;
    border: 1px solid rgb(32, 15, 15);
    box-shadow: 2px 2px 8px 4px #a03131d1;
    border-radius: 15px;
    font-family: sans-serif;
    margin-left: 53%;
    margin-top: -30%;
}
.tarjeta-3{
background: black;
display:flex;
flex-direction:column;
justify-content:space-between;
width:420px;
border: 1px solid rgb(32, 15, 15);
box-shadow: 2px 2px 8px 4px #a03131d1;
border-radius:15px;
font-family: sans-serif; 
margin-top: 5%;
margin-left: 3%;
}
.tarjeta-4{
    background: black;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    width: 420px;
    border: 1px solid rgb(32, 15, 15);
    box-shadow: 2px 2px 8px 4px #a03131d1;
    border-radius: 15px;
    font-family: sans-serif;
    margin-left: 53%;
    margin-top: -30.7%;
}
h4.textimg-sec2 {
    color: white;
    position: absolute;
    margin-left: 9%;
    margin-top: -3%;
}
h4.textimg1-sec2 {
    color: white;
    position: absolute;
    margin-left: 9%;
    margin-top: -3%;
}
h4.textimg2-sec2 {
    color: white;
    position: absolute;
    margin-left: 9%;
    margin-top: -3%;
}
h4.textimg3-sec2 {
    color: white;
    position: absolute;
    margin-left: 9%;
    margin-top: -3%;
}
/* tarjetas seccion tres */
.tarjeta-sec2{
display:flex;
flex-direction:column;
justify-content:space-between;
width:420px;
border: 1px solid rgb(32, 15, 15);
box-shadow: 2px 2px 8px 4px #a03131d1;
border-radius:15px;
font-family: sans-serif;
margin-left: 3%;
}
div a {text-decoration: none;}
.tarjeta-2-sec2{
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    width: 420px;
    border: 1px solid rgb(32, 15, 15);
    box-shadow: 2px 2px 8px 4px #a03131d1;
    border-radius: 15px;
    font-family: sans-serif;
    margin-left: 53%;
    margin-top: -59%;
}
.tarjeta-3-sec2{
display:flex;
flex-direction:column;
justify-content:space-between;
width:420px;
border: 1px solid rgb(32, 15, 15);
box-shadow: 2px 2px 8px 4px #a03131d1;
border-radius:15px;
font-family: sans-serif; 
margin-top:5% ;
margin-left: 3%;
}
.tarjeta-4-sec2{
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    width: 420px;
    border: 1px solid rgb(32, 15, 15);
    box-shadow: 2px 2px 8px 4px #a03131d1;
    border-radius: 15px;
    font-family: sans-serif;
    margin-left: 53%;
    margin-top: -59%;
}
.titulo{
font-size: 24px;
padding: 10px 10px 0 10px;
}
.cuerpo{
    padding: 7px;
    background-color: #890000;
    border-radius: 43px;
}
.pie{
background: #442929;
border-radius:0 0 15px 15px;
padding: 10px;
text-align:center;
color: white;
}
.pie a{
text-decoration: none;
}
.pie a:after {
position: absolute;
top: 0;
right: 0;
bottom: 0;
left: 0;
z-index: 1;
color: white;
}
.pie:hover{
    background:radial-gradient( circle, black, #1162ac);
    transition-duration: 2s, 3s, 2s, 3s;
}
img.img-sec2-1 {
    width: 100% !important;
    
}
img.img-sec2-1:hover {
    filter: blur(4px);
    -webkit-transform: scale(1.5);
    transform: scale(1.2);
    transition-duration: 2s, 3s, 2s, 3s;
}
img.img-sec2-2 {
   
   width: 100% !important;
   border-radius: 20px;
   height: 17vw;
}
img.img-sec2-2:hover {
    filter: blur(4px);
    -webkit-transform: scale(1.5);
    transform: scale(1.2);
    transition-duration: 2s, 3s, 2s, 3s;
}
img.img-sec2-3 {
    width: 100% !important;
    height: 17vw;
}
img.img-sec2-3:hover {
    filter: blur(4px);
    -webkit-transform: scale(1.5);
    transform: scale(1.2);
    transition-duration: 2s, 3s, 2s, 3s;
}
img.img-sec2-4 {
    width: 100% !important;
    height: 17vw;
}
img.img-sec2-4:hover {
    filter: blur(4px);
    -webkit-transform: scale(1.5);
    transform: scale(1.2);
    transition-duration: 2s, 3s, 2s, 3s;
}
    </style>
</head>
<body>
    <div class="row">
        <div class="rounded-3" style="background: rgb(0,0,0);background: linear-gradient(90deg, rgba(0,0,0,1) 0%, rgba(61,0,0,1) 35%);;color:aliceblue;font-size: 1.6rem;">
        <h1 class="text-center  mt-2" style="font-size: 2.5rem;">Nombre Página / Logo</h1>
        <p class="text-center" style="font-size: 1.5rem;">Alguna frase</p>
        <hr style="margin: 0;">
        <nav class="navbar navbar-expand-lg">
            <div class="container-fluid">
                <a class="navbar-brand" href="../" style="color: aliceblue;font-size: 2rem;">Logo</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav">
                        <li class="nav-item">
                        <a class="nav-link" href="../Noticias" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Noticias</a>
                        </li>
                        <li class="nav-item">
                        <a class="nav-link" href="#" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Análisis</a>
                        </li>
                        <li class="nav-item">
                        <a class="nav-link" href="../Guias" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Guías</a>
                        </li>
                        <li class="nav-item">
                        <a class="nav-link active" href="../Foro" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Foro</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
        </div>
    </div> 
    <div class="row d-flex justify-content-center">
        <div class="container-fluid w-75">
            <div>
                <h2 class="mt-5 text-center" style="background-color:black;color:aliceblue;">ANÁLISIS DE VIDEOJUEGOS</h2>
            </div>
            <div class="mt-3">
                <p style="text-align:justify;">
                    En esta página encontrarás todos los análisis de videojuegos que tenemos. ¿Estás pensando en comprar un videojuego? En esta web contamos con un equipo de analistas especializados para analizar los últimos lanzamientos valorando aspectos como los gráficos, el sonido, la jugabilidad, el rendimiento, los diferentes modos de juego y otros aspectos en su conjunto y le aplicamos una nota de 1 a 10, que representa su calidad general, para que te ayude a decidir qué juegos merecen la pena, cuáles cumplen las expectativas y cuáles se quedan atrás.
                </p>
            </div>
            <div class="container-fluid ">
                <div class="col-12">
                    <div class="tarjeta">
                        <div class="cuerpo"> 
                            <img src="https://media.vandal.net/i/300x160/8-2022/20228101316025_1.jpg"  class="img-sec2-2" style="width: 15%;border-radius: 10px;" alt="muestra"><h4 class="textimg-sec2">Spider-Man: Remastered</h4>              
                        </div>                
                        <a href="#"><div class="pie">Analizamos la versión para PC del videojuego de Insomniac Games que llega a nuestros ordenadores con una versión muy trabajada para ofrecer la mejor calidad técnica y rendimiento posibles.</div></a>
                    </div>
                </div>
                    
                        <div class="tarjeta-2">
                        <div class="cuerpo"> 
                            <img src="https://media.vandal.net/i/300x160/7-2022/20227268545686_1.jpg"  class="img-sec2-2" style="width: 15%;border-radius: 10px;" alt="muestra"><h4 class="textimg1-sec2">Xenoblade Chronicles 3</h4>                            
                        </div>
                        
                        <a href="#"><div class="pie">Monolith Soft lo vuelve a hacer para traernos uno de los mejores y más descomunales JRPG de los últimos años.</div></a>

                        </div>
                        <div class="tarjeta-3">
                            <div class="cuerpo"> 
                                <img src="https://media.vandal.net/i/300x160/5-2022/202253130458_1.jpg"  class="img-sec2-3" style="width: 15%;border-radius: 10px;" alt="muestra"><h4 class="textimg2-sec2">Trek to Yomi</h4>                            
                            </div>
                        
                            <a href="#"><div class="pie">Una aventura de samuráis espectacular e impactante, pero que sabe a poco en los aspectos jugables.</div></a>
    
                            </div>
                            <div class="tarjeta-4">
                                <div class="cuerpo"> 
                                    <img src="https://media.vandal.net/i/300x160/4-2022/20224161753156_1.jpg"  class="img-sec2-4" style="width: 15%;border-radius: 10px;" alt="muestra"><h4 class="textimg3-sec2">  Chernobylite</h4>                 
                                </div>
                                
                                <a href="#"><div class="pie">Chernobylite, la interesante aventura de The Farm 51, se adapta a las nuevas consolas y soluciona problemas técnicos que sufría la anterior generación.</div></a>
        
                                </div>
                    
                            </div>
                        </div>
                        
                        <!--seccion 3-->
                    </div>                   
                </div>
            </div>                             
        </div>
    </div>
</body>
</html>
    ''')
