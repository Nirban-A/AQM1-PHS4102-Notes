-- Fenced divs produced by build_pdfs.py (class "adm", attributes type/title)
-- become tcolorbox environments; single-image paragraphs are centred.
local known = {thm=1, prob=1, solution=1, intuition=1, studynote=1, memory=1,
               examtip=1, verification=1, mistakes=1, exam=1, book=1}

function Div(el)
  if el.classes:includes("adm") then
    local typ = el.attributes["type"] or "studynote"
    if not known[typ] then typ = "studynote" end
    local title = el.attributes["title"] or ""
    local b = {pandoc.RawBlock("latex", "\\begin{adm" .. typ .. "}{" .. title .. "}")}
    for _, x in ipairs(el.content) do table.insert(b, x) end
    table.insert(b, pandoc.RawBlock("latex", "\\end{adm" .. typ .. "}"))
    return b
  end
end

function Para(el)
  if #el.content == 1 and el.content[1].t == "Image" then
    return {pandoc.RawBlock("latex", "\\begin{center}"), el, pandoc.RawBlock("latex", "\\end{center}")}
  end
end
