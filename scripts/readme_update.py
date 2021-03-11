#!/usr/bin/env python3

import os
import glob

REPO = "ktmeaton/pixelart"
REPO_URL = "https://github.com/ktmeaton/pixelart"
IMG_SRC_GLOBS = ["*{}.gif", "*{}_96px.png","*{}.png"]

SPRITESHEET_GLOB = "*_spritesheet.png"
TILE_PER_ROW = 6
TOC = ["Pixilart Daily Challenge", "Studies", "Sprites", "Avatars", "Fonts", "Logos", "Notes"]
DAILIES_ELEMENT = """    <td align='center'>
      <a href='{}'>
        <img src='{}' width='100px;' alt=''/>
        <br /> 
        <br />
        <sub>
          <b>{}</b>
        </sub>   
      </a>
      <br />
      <small>{}</small>
      <br />       
      <a href='https://www.pixilart.com/search?term={}'>#{}</a>"""

AVATARS_ELEMENT = """    <td align='center'>
        <a href='{}'>
            <img src='{}' width='100px;' alt=''/>
            <br />
            <sub>
                <b>{}</b>
            </sub>
        </a>
    </td>"""  

STUDIES_ELEMENT = """    <td align='center'>
        <a href='{}'>
            <img src='{}' width='200px;' alt=''/>
            <br />
            <sub>
                <b>{}</b>
            </sub>
        </a>
    </td>"""    

LOGOS_ELEMENT = """    <td align='center'>
        <a href='{}'>
            <img src='{}' width='100px;' alt=''/>
            <br />
            <sub>
                <b>{}</b>
            </sub>
        </a>
    </td>"""  

FONTS_ELEMENT = """    <td align='center'>
        <a href='{}'>
            <img src='{}' width='700px;' alt=''/>
            <br />
            <sub>
                <b>{}</b>
            </sub>
        </a>
    </td>"""      

SPRITESHEET_ELEMENT = """\t<br />
        <a href='{}'>spritesheet</a>"""

script_dir = os.path.dirname(os.path.realpath(__file__))
project_dir = os.path.dirname(script_dir)
dailies_dir = os.path.join(project_dir, "dailies")
avatars_dir = os.path.join(project_dir, "avatars")
logos_dir = os.path.join(project_dir, "logos")
sprites_dir = os.path.join(project_dir, "sprites")
fonts_dir = os.path.join(project_dir, "fonts")
studies_dir = os.path.join(project_dir, "studies")

# -----------------------------------------------------------------------------
# Header
print("# Pixelart\n")

# -----------------------------------------------------------------------------
# TOC
print("## Table of Contents\n")

for i in range(0, len(TOC) ,1):
    section_pretty = TOC[i]
    section_plain = section_pretty.lower().replace(" ","-")
    print(
        "{}. [{}]({})".format(i + 1, section_pretty,REPO_URL + "#" + section_plain)
        )
print("")

# -----------------------------------------------------------------------------
# Dailies

print("## [Pixilart Daily Challenges](https://www.pixilart.com/challenges)\n")

# Tables organized by month
for year in os.listdir(dailies_dir):
    # ex. 2021
    year_dir = os.path.join(dailies_dir, year)
    for month in os.listdir(year_dir):
        # ex. 02
        row_counter = 1
        print("### {} {}\n".format(year, month))
        print("<table>")
        month_dir = os.path.join(year_dir, month)
        for day in range(1,32,1):
            # ex. 25_elevator_CN-Tower_spritesheet.png
            day_prefix = os.path.join(month_dir, str(day) + "_*")
            day_files = glob.glob(day_prefix)
            if len(day_files) == 0: continue
            first_match = day_files[0]

            # Parse out the following info
            # 1) Img src: dailies/2021/02/25_elevator_CN-Tower.gif
            # 2) Date: 2021-02-25
            # 3) Prompt: Elevator
            # 4) Title: CN Tower
            # 5) Optional:
            #   5a) Spritesheet: dailies/2021/02/25_elevator_CN-Tower_spritesheet.png

            # Parse out info from match filename
            split_match = first_match.split("_")
            # Get the title of the art piece
            title_plain = split_match[2].split(".")[0]

            # -----------------------------------------------------------------
            img_src = ""
            # 1) Img src
            for ext in IMG_SRC_GLOBS:
                ext_query = day_prefix + ext.format(title_plain)
                res = glob.glob(ext_query)
                # If we've found a matching file, break and use it                
                if len(res) > 0:
                    file_name = os.path.basename(res[0])
                    img_src = "dailies/{}/{}/{}".format(year, month, file_name)
                    break
            
            # -----------------------------------------------------------------
            # 2) Date     
            date = "{}-{}-{}".format(year,month,day) 

            # -----------------------------------------------------------------
            # 3) Prompt
            prompt = split_match[1]

            # -----------------------------------------------------------------
            # 4) Title
            title_pretty = title_plain.replace("-", " ").title()   
            # Manual edits
            title_pretty = title_pretty.replace("Cn ", "CN ")          

            # OUTPUT
            # Print a new table row if needed
            if row_counter == 1:
                print("  <tr>")

            print(DAILIES_ELEMENT.format(
                img_src,      # <a href=...
                img_src,      # <img src=...
                title_pretty, # <b>title</b>
                date,         # <small>xxxx-xx-xx</small>
                prompt,       # https://www.pixilart.com/search?term=...
                prompt,       # #prompt
                )
            )
            # -----------------------------------------------------------------
            # 5a) Optional: Spritesheet
            spritesheet_query = day_prefix + SPRITESHEET_GLOB
            res = glob.glob(spritesheet_query)
            if len(res) > 0:
                file_name = os.path.basename(res[0])
                spritesheet = "dailies/{}/{}/{}/{}".format(year, month, day, file_name)
                print(SPRITESHEET_ELEMENT.format(spritesheet))

            # Close table element
            print("    </td>")

            # Increment the row counter
            row_counter += 1
            if row_counter > TILE_PER_ROW:
                print("  </tr")
                row_counter = 1

        if row_counter <= TILE_PER_ROW:
            print("  </tr>")        
        print("</table>\n")

# -----------------------------------------------------------------------------
# Studies

print("## Studies\n")
print("<table>")

for study in os.listdir(studies_dir):
    study_dir = os.path.join(studies_dir, study)
    print("  <tr>")  
    print("  </tr>")
    # Search for gifs and images
    img_src = ""
    for ext in IMG_SRC_GLOBS:
        ext_query = study_dir + "/" + ext.format("")
        res = glob.glob(ext_query)  
        if len(res) == 0: continue

        # link to gif/image
        print(
            "" 
            + "    <td align='center'>\n"
            + "      <a href='studies/{}/{}.png'>".format(study, study)
        )
        # Elements for each individual gif
        for src in res:
            file_name = os.path.basename(src)
            img_src = "studies/{}/{}".format(study, file_name)
            print("""        <a href='{}'>
                <img src='{}' width='200px;' alt=''/> 
            </a>""".format(img_src, img_src))   
        # meta information
        print(
            """        <br />
            <sub>
              <b>{}</b>
            </sub>
        </a>
        <br />
        <a href='studies/{}/credits.txt'>credits</a> """.format(study, study)           
        )
        print("    </td>")    
    print("  </tr>")        
print("</table>\n")

# -----------------------------------------------------------------------------
# Sprites

print("## Sprites\n")
print("<table>")

for sprite in os.listdir(sprites_dir):
    sprite_dir = os.path.join(sprites_dir, sprite)
    print("  <tr>")
    # Search for gifs
    gif_query = os.path.join(sprite_dir, "*.gif")
    res = glob.glob(gif_query)
    if len(res) > 0:
        # link to master spritesheet
        print(
            "" 
            + "    <td align='center'>\n"
            + "      <a href='sprites/{}/{}_spritesheet.png'>".format(sprite, sprite)
        )
        # Elements for each individual gif
        for gif in res:
            file_name = os.path.basename(gif)
            img_src = "sprites/{}/{}".format(sprite, file_name)
            print("""        <a href='{}'>
                <img src='{}' width='100px;' alt=''/> 
            </a>""".format(img_src, img_src))   
        # sprite meta information
        print(
            """        <br />
            <sub>
              <b>{}</b>
            </sub>
        </a>
        <br />
        <a href='sprites/{}/{}_spritesheet.png'>spritesheet</a> """.format(sprite, sprite, sprite)           
        )
        print("    </td>")    
    print("  </tr>")

print("</table>\n")

# -----------------------------------------------------------------------------
# Avatars

print("## Avatars\n")
print("<table>")

row_counter = 1
for avatar in os.listdir(avatars_dir):
    avatar_dir = os.path.join(avatars_dir, avatar)
    img_src = ""
    for ext in IMG_SRC_GLOBS:
        ext_query = avatar_dir + "/" + ext.format("")
        res = glob.glob(ext_query)
        # If we've found a matching file, break and use it                
        if len(res) > 0:
            file_name = os.path.basename(res[0])
            img_src = "avatars/{}/{}".format(avatar, file_name)
            break

    # OUTPUT
    # Print a new table row if needed
    if row_counter == 1:
        print("  <tr>") 
                
    print(AVATARS_ELEMENT.format(
        img_src,      # <a href=...
        img_src,      # <img src=...
        avatar,       # <b>title</b>
        )      
    )

    # Increment the row counter
    row_counter += 1
    if row_counter > TILE_PER_ROW:
        print("  </tr")
        row_counter = 1

print("""  </tr>
</table>
""")    

# -----------------------------------------------------------------------------
# Logos

print("## Logos\n")
print("<table>")

row_counter = 1
for logo in os.listdir(logos_dir):
    logo_dir = os.path.join(logos_dir, logo)
    logo_path = os.path.join(logo_dir, logo + ".png")
    res = glob.glob(logo_path)
    if len(res) > 0:
        file_name = os.path.basename(res[0])
        img_src = "logos/{}/{}".format(logo, file_name)

        # OUTPUT
        # Print a new table row if needed
        if row_counter == 1:
            print("  <tr>") 
                  
        print(LOGOS_ELEMENT.format(
            img_src,      # <a href=...
            img_src,      # <img src=...
            logo,       # <b>title</b>
            )      
        )

        # Increment the row counter
        row_counter += 1
        if row_counter > TILE_PER_ROW:
            print("  </tr")
            row_counter = 1

print("""  </tr>
</table>
""")    

# -----------------------------------------------------------------------------
# Fonts

print("## Fonts\n")
print("<table>")

row_counter = 1
for font in os.listdir(fonts_dir):
    font_dir = os.path.join(fonts_dir, font)
    font_path = os.path.join(font_dir, font + ".png")
    res = glob.glob(font_path)
    if len(res) > 0:
        file_name = os.path.basename(res[0])
        img_src = "fonts/{}/{}".format(font, file_name)

        # OUTPUT
        # Print a new table row if needed
        if row_counter == 1:
            print("  <tr>") 
                  
        print(FONTS_ELEMENT.format(
            img_src,      # <a href=...
            img_src,      # <img src=...
            font,       # <b>title</b>
            )      
        )

        # Increment the row counter
        row_counter += 1
        if row_counter > TILE_PER_ROW:
            print("  </tr")
            row_counter = 1

print("""  </tr>
</table>
""")    

# -----------------------------------------------------------------------------
# Notes
print("""## Notes

### Spritesheets

```yaml
- Tile display resolution: 96 px
- Download: Original
- Background: Transparent
```
### Animation

```yaml
- Tile display resolution: 96 px
- Download: 320 px
- Background: White
```
""")