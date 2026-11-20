# Таблички-карточки в HTML — как собирать

Было: картинка 900×506 из выгрузки «Взнания» (мылится, не масштабируется).
Стало: тот же смысл, но живым HTML в блоке `text`.

## Что можно, а что нельзя

Платформа чистит HTML функцией `lessonHtml`. Разрешены теги:
`p div span br b strong i em u s mark sup sub small h1..h6 ul ol li blockquote hr
table thead tbody tfoot tr td th caption img audio source a figure figcaption`.
Атрибуты: `style`, `class`, `title`, `role`, `aria-label` у всех; `src/alt/width/height`
у `img`; `colspan/rowspan` у `td`/`th`.

**В `style` нельзя `url(...)`** — атрибут снимается целиком. Фоновых картинок нет,
только цвет. Никаких `<script>`, `<style>`, классов из внешних CSS (их нет).

## Каркас

```html
<div style="max-width:860px;border:1px solid #E6E0D8;border-radius:14px;overflow:hidden;font-size:16px;line-height:1.45">
  <div style="background:#E8732A;color:#fff;padding:10px 16px;font-weight:700">Unit 1 · to be · утвердительная форма</div>
  <div style="padding:14px 16px;background:#fff">
    … содержимое …
  </div>
</div>
```

Цвет шапки берём из самой картинки: оранжевый `#E8732A`, фиолетовый `#6B4CC4`,
синий `#2F6FB8`, зелёный `#2E9E6B`, розовый `#D94A77`.

## Строки «английское — русское»

```html
<table style="width:100%;border-collapse:collapse">
  <tr>
    <td style="padding:8px 10px;border-bottom:1px solid #F0ECE6"><b>I'm ten years old.</b></td>
    <td style="padding:8px 10px;border-bottom:1px solid #F0ECE6;color:#6B7280">Мне десять лет.</td>
  </tr>
</table>
```

## Грамматическая таблица

```html
<table style="width:100%;border-collapse:collapse;background:#FFF8EF">
  <tr>
    <th style="text-align:left;padding:8px 10px;color:#B4530F">Подлежащее</th>
    <th style="text-align:left;padding:8px 10px;color:#B4530F">Полная</th>
    <th style="text-align:left;padding:8px 10px;color:#B4530F">Краткая</th>
  </tr>
  <tr>
    <td style="padding:8px 10px">I</td>
    <td style="padding:8px 10px"><b>am</b></td>
    <td style="padding:8px 10px">I'm</td>
  </tr>
</table>
```

## Предупреждение / ловушка

```html
<p style="margin:12px 0 0;padding:10px 12px;background:#FDF0F4;border-left:4px solid #D94A77;border-radius:8px">
  ⚠️ «She ARE» ✗ → «She IS» ✓ · апостроф заменяет букву: she's = she is
</p>
```

## Правила содержания

- Переносим ВЕСЬ текст с картинки слово в слово: английские фразы, русские переводы,
  заголовок, предупреждения. Ничего не выдумываем и не сокращаем.
- Английское — `<b>`, русское рядом — серым (`color:#6B7280`).
- Эмодзи с картинки сохраняем.
- Ширина не задаётся в пикселях у ячеек: таблица тянется, на телефоне читается.
- Картинок внутри нет (кроме случая, когда на карточке есть рисунок предмета —
  тогда `<img src="…" alt="" style="height:120px">` со ссылкой на тот же файл).
