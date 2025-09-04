# SciCAR 2025: Vibe Coding
Hier findet ihr die Materialien, Links und weitere Informationen aus unserem Workshop.


## Was ist Vibe Coding?
- LLMs nicht nur als Coding-Assistenz, sondern als **Übersetzer von natürlicher Sprache in Code**.  
- Entwickler:innen interagieren mit dem LLM, nicht mehr direkt mit dem Code.  
- Ziel: schnelleres Prototyping, kostengünstige Experimente, Umsetzung komplexer Ideen.  

## Warum Vibe Coding?
- **Zeit:** schnelle Iteration, Hypothesen testen  
- **Kosten:** günstige Prototypen statt langer Entwicklungszyklen  
- **Neue Möglichkeiten:** komplexe oder aufwändige Projekte einfacher umsetzbar  

## Tools
- **Claude Code** – starke Performance beim Vibecoding  
- **Cursor** – IDE mit LLM-Integration (Autocomplete, .cursorrules etc.)  
- **Github Copilot** – Code-Reviews, Autocomplete  

## Caude Code installieren:
<a href="http://www.youtube.com/watch?feature=player_embedded&v=NQNrPaDPMiA
" target="_blank"><img src="http://img.youtube.com/vi/NQNrPaDPMiA/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>
\
Claude Code Dokumentation: [docs.anthropic.com](https://docs.anthropic.com/en/docs/claude-code/overview)\
Für die Nutzung in vscode empfehlen wir das Plugin [Claude Code for VSCode](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code)

## Best Practices
- **Kontext:** Projektbeschreibung, Tech-Stack, Coding Conventions für das Projekt in .cursor/rules oder CLAUDE.md schreiben. 
Beispiel-Templates findet ihr hier: [cursor.directory](https://cursor.directory/) oder hier [awsome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules)
- **Prompting:** präzise, wie an einen Kollegen formulieren  
- **Iteration:** häufig committen, kurze Chats, Arbeitsschritte trennen  

## Risiken & Herausforderungen
cursorrules können versteckte Prompts enthalten, die scädlichen Code generieren ([ascii smuggling](https://embracethered.com/blog/ascii-smuggler.html)).\
Um versteckte Zeichen in Markdownfiles zu erkennen kann es hilfreich sein, in den vscode/cursor settings versteckte Zeichen in Markdown Files einzublenden.

command+shift+p > "Preferences: Open User Settings (JSON)" > folgendes Snippet einfügen und speichern
```
"[markdown]":  {
	"editor.unicodeHighlight.invisibleCharacters": true,
}
```
\
\
Auch MCP Server können Sicherheitsrisiken bergen. Hier ein Artikel von Docker zu dem Thema: [MCP Horror Stories: The Security Issues Threatening AI Infrastructure
](https://www.docker.com/blog/mcp-security-issues-threatening-ai-infrastructure/)