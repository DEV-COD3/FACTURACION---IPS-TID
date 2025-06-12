Analisis del problema -> Permitir el cambio entre modos de facturacion de forma dinamica, comoda e intuituva para el personal financiero
  En el plantel empresarial se maneja un aplicativo web de gestion general, el cual está alojado en un servidor local, dentro de la interfaz grafica hay 2 opciones para los modos de facturacion
  (Esto debido a que la ley distingue los procesos de factiracion para 2 escenarios de auxiliar y paciente), la opcion está presente en la interfaz grafica default, pero el area financiera tiene problemas recordando como encontrarla,
  por ende suelen recurrir al area de sistemas para efectuar este cambio; lo cual generaba mucha friccion en las actividades diarias del area.

Solucion -> Crear un aplicativo de escritorio que replique la consulta del front default.
A través de la credenciales de acceso local, se procede con la replica del fetch que se efectua con el botón del front.
Se genera una interfaz con 2 botones (cada uno genera un fetch diferente), a su vz se implementa un label que adquiere el valor segun la facturacion activa en el momento

Se compiña y entrega con su respectivo SaaS
