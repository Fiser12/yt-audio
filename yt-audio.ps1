Add-Type -AssemblyName Microsoft.VisualBasic

$videoUrl = [Microsoft.VisualBasic.Interaction]::InputBox(
    "Introduce la URL del video de YouTube:",
    "Descargar Contenido de YouTube",
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
)

if ([string]::IsNullOrWhiteSpace($videoUrl)) {
    Write-Host "No se proporcionó una URL. Saliendo..."
    exit
}

$modo = [Microsoft.VisualBasic.Interaction]::InputBox(
    "Selecciona el modo de descarga (audio/video):",
    "Modo de Descarga",
    "audio"
)

if ($modo -ne "audio" -and $modo -ne "video") {
    $modo = "audio"
}

Write-Host "Descargando contenido del video en modo $modo: $videoUrl"

$env:MODO_DESCARGA = $modo
docker-compose run --rm downloader $videoUrl