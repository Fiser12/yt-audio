Add-Type -AssemblyName Microsoft.VisualBasic

$videoUrl = [Microsoft.VisualBasic.Interaction]::InputBox(
    "Introduce la URL del video de YouTube:",
    "Descargar Audio de YouTube",
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
)

if ([string]::IsNullOrWhiteSpace($videoUrl)) {
    Write-Host "No se proporcionó una URL. Saliendo..."
    exit
}

Write-Host "Descargando audio del video: $videoUrl"

docker run --rm -v "$(Resolve-Path ./):/code/downloads" ghcr.io/fiser12/yt-audio:main $videoUrl