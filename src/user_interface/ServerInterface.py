from src.calculator.Calculator import Calculator
from src.database.DbDao import DbDao
from src.database.database import Database
from src.database.database_initializator import intitialize_database

from http.server import BaseHTTPRequestHandler
import urllib.parse


class ServerInterface(BaseHTTPRequestHandler):



    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def _html(self, message):
        """This just generates an HTML document that includes `message`
        in the body. Override, or re-write this do do more interesting stuff.
        """
        content = f"{message}"
        return content.encode("utf8")  # NOTE: must return a bytes object!

    def do_GET(self):
        historique= None
        calculator = Calculator()
        dbDao = DbDao()
        historique = dbDao.getAllCalculs()
        formule = ""
        resultat = ""
        tmp = ""
        toCalculate = str(urllib.parse.unquote(self.path)[1:len(urllib.parse.unquote(self.path))])
        result = 0
        try:
            if(len(toCalculate) > 0):
                result = calculator.calculate(toCalculate)
        except Exception:
            result = 0
        if(historique == None):
            intitialize_database()
        else :
            compteurHistoric = 0
            for his in historique:
                tmp = his[1]
                formule = "<li id='hist" + str(compteurHistoric) + "'>"+tmp + " = " + str(his[2])+"</li>"
                compteurHistoric = compteurHistoric + 1
                resultat = resultat+formule
        
        resultat = "<ul>"+resultat+"</ul>";    
        self._set_headers()
        self.wfile.write(self._html("""
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="utf-8">
                <title>Titre de la page</title>
            </head>
    
            <body>
                <div>
                    <label id="screen">0</label>
                    <div style="display: block">
                        <button type="button" id="num1">1</button>
                        <button type="button" id="num2">2</button>
                        <button type="button" id="num3">3</button>
                        <button type="button" id="opAdd">+</button>
                        <button type="button" id="parOpen">(</button>
                    </div>
                    <div style="display: block">
                        <button type="button" id="num4">4</button>
                        <button type="button" id="num5">5</button>
                        <button type="button" id="num6">6</button>
                        <button type="button" id="opMin">-</button>
                        <button type="button" id="parClose">)</button>
                    </div>
                    <div style="display: block">
                        <button type="button" id="num7">7</button>
                        <button type="button" id="num8">8</button>
                        <button type="button" id="num9">9</button>
                        <button type="button" id="opMult">x</button>
                        <button type="button" id="opDiv">/</button>
                    </div>
                    <div style="display: block">
                        <button type="button" id="clear">C</button>
                        <button type="button" id="num0">0</button>
                        <button type="button" id="equal">=</button>
                    </div>
                </div>
               
                <div>
                    <button type="button" id="historique">Historique</button>
                    <button type="button" id="hide">Hide</button>
                </div>
               
                <div id="histoResult">
               """+resultat+"""
                </div>
               
                <script>
                    var special = false;
                    
                    document.getElementById("historique").addEventListener('click', event => {
                        document.getElementById("histoResult").innerHTML = \""""+resultat+"""\";
                    });
                    document.getElementById("hide").addEventListener('click', event => {
                        document.getElementById("histoResult").innerText = "";
                    });
                    document.getElementById("num0").addEventListener('click', event => {
                        putElmt("0");
                    });
                    document.getElementById("num1").addEventListener('click', event => {
                        putElmt("1");
                    });
                    document.getElementById("num2").addEventListener('click', event => {
                        putElmt("2");
                    });
                    document.getElementById("num3").addEventListener('click', event => {
                        putElmt("3");
                    });
                    document.getElementById("num4").addEventListener('click', event => {
                        putElmt("4");
                    });
                    document.getElementById("num5").addEventListener('click', event => {
                        putElmt("5");
                    });
                    document.getElementById("num6").addEventListener('click', event => {
                        putElmt("6");
                    });
                    document.getElementById("num7").addEventListener('click', event => {
                        putElmt("7");
                    });
                    document.getElementById("num8").addEventListener('click', event => {
                        putElmt("8");
                    });
                    document.getElementById("num9").addEventListener('click', event => {
                        putElmt("9");
                    });
                    document.getElementById("opAdd").addEventListener('click', event => {
                        putElmt(" +");
                        special = true;
                    });
                    document.getElementById("opMin").addEventListener('click', event => {
                        putElmt(" -");
                        special = true;
                    });
                    document.getElementById("opMult").addEventListener('click', event => {
                        putElmt(" *");
                        special = true;
                    });
                    document.getElementById("opDiv").addEventListener('click', event => {
                        putElmt(" /");
                        special = true;
                    });
                    document.getElementById("parOpen").addEventListener('click', event => {
                        putElmt(" (");
                        special = true;
                    });
                    document.getElementById("parClose").addEventListener('click', event => {
                        putElmt(" )");
                        spcial = true;
                    });
                    document.getElementById("clear").addEventListener('click', event => {
                        document.getElementById("screen").innerText = "0";
                    });
                     
                    document.getElementById("equal").addEventListener('click', event => {
                        document.location.href = "http://localhost:8000/" + document.getElementById("screen").innerText;
                    });
                    
                    function putElmt(element) {
                        if(special) {
                            element = " " + element;
                            special = false;
                        }
                        if(document.getElementById("screen").innerText == "0") {
                            document.getElementById("screen").innerText = "";
                        }
                        document.getElementById("screen").innerText = document.getElementById("screen").innerText + element;
                    }
                </script>
            </body>
 
        </html>
        """ + "<script>var value = \""+str(result)+"\"; value = decodeURI(value); document.getElementById(\"screen\").innerText = value;</script>"))
