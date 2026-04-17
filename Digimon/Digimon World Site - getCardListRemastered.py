import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Send a GET request to the URL
url = 'https://world.digimoncard.com/cards/?search=true&category=522033'
response = requests.get(url)
html_content = response.content

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Step 3: Get Card Details for Every Card
cards = soup.select('.image_lists_item')
# print(cards[0])

keywords = []
final_card_list = []

# Step 4: Reformat Cards Data
for card in cards:
        final_card = []

    # 4.1 Card Image Url
        # Extract Image Url Data
        image_url = card.select('.cardImgInner')
        # Reformat
        html_element, imgurl = str(image_url).rsplit('src="../', 1)
        imgurl = imgurl.split('"/>')[0]
        final_image_url_text = "https://world.digimoncard.com/" + imgurl
        # print(final_image_url_text)

    # 4.2 Card ID Code
        # Extract
        card_id = card.select('.cardNo')
        # Reformat
        html_element, idcode = str(card_id).rsplit('cardNo">', 1)
        idcode = idcode.split('</li>')[0]
        idcode = idcode.strip()
        # print(idcode)

    # 4.3 Card Name
        # Extract
        card_name = card.select('.cardTitle')
        # Reformat
        html_element, name = str(card_name).rsplit('cardTitle">', 1)
        name = name.split('</div>')[0]
        name = name.strip()
        # print(name)

    # 4.4   Card Color
        # Extract
        card_color = card.select_one('.cardColor')
        # Reformat
        if card_color:
            color_spans = card_color.find_all('span')
            colors = [span.get_text(strip=True) for span in color_spans if span.get_text(strip=True)]
            colors_str = '/'.join(colors)
        else:
            colors_str = ''
        # print(colors_str)

    # 4.5   Card Rarity
        # Extract
        card_rarity = card.select('.cardRarity')
        # print(card_rarity)
        # Reformat
        if card_rarity != [] :
            [html_el, rarity] = str(card_rarity).rsplit('cardRarity">', 1)
            rarity = rarity.split('</li>')[0]
            rarity = rarity.strip()
        else :
            rarity = '-'
        # print(rarity)

    # 4.6   Card Type
        # Extract
        card_type = card.select('.cardType')
        # Reformat
        if card_type != [] :
            html_element, ctype = str(card_type).rsplit('cardType">',1)
            ctype = ctype.rsplit('</li>')[0]
            ctype = ctype.strip()
        else :
            ctype = '-'
        # print(type)

    # 4.7   Card Level
        # Extract
        card_level = card.select('.cardLv')
        # Reformat
        if card_level != [] :
            html_element, level = str(card_level).rsplit('cardLv">',1)
            level = level.rsplit('</li>')[0]
            level = level.strip()
        else :
            level = '-'
        # print(level)

    # 4.8   Copies Owned
        owned = 0
        # print(owned)

    # 4.9   Art Version
        # Extract
        card_art = card.select('.cardParallel')
        # Reformat
        if card_art != [] :
            html_element, art = str(card_art).rsplit('cardParallel">',1)
            art = art.rsplit('</li>')[0]
            art = art.strip()
        else :
            art = 'Basic Art'
        # print(art)

    # 4.10  cardInfoTit - cardInfoData Pairs
        info_pairs = {}
        for dt in card.find_all('dt', class_= 'cardInfoTit'):
            label = dt.get_text(strip=True)
            dd = dt.find_next_sibling('dd', class_='cardInfoData')
            if dd:
                info_pairs[label] = dd.get_text(strip=True)
        # print(labels)

        form = info_pairs.get('Form', '-')
        attribute = info_pairs.get('Attribute', '-')
        type = info_pairs.get('Type', '-')
        dp = info_pairs.get('DP', '-')
        cost = info_pairs.get('Cost', '-')
        dcost1 = info_pairs.get('Digivolve Cost 1', '-')
        dcost2 = info_pairs.get('Digivolve Cost 2', '-')
        pack = info_pairs.get('Notes', '-').strip('CARD LISTPRODUCTS')

        # print(info_pairs)
        # print(form)
        # print(attr)
        # print(pack)

    # 4.11  cardInfoTitSmall - cardInfoData Pairs
        info_pairs_small = {}
        for dt in card.find_all('dt', class_= 'cardInfoTitSmall'):
            label = dt.get_text(strip=True)
            dd = dt.find_next_sibling('dd', class_='cardInfoData')
            if dd:
                info_pairs_small[label] = dd.get_text(strip=True)
        # print(labels)
        # print(info_pairs_small)

        spdcost = info_pairs_small.get('[Special Digivolution Condition]', '-')
        spplcond = info_pairs_small.get('[Special Play Condition]', '-')
        effect = info_pairs_small.get('[Effect]', '-')
        ieffect = info_pairs_small.get('[Inherited Effect]', '-')
        seffect = info_pairs_small.get('[Security Effect]', '-')
        linkcond = info_pairs_small.get('[Link Condition]', '-')
        linkdp = info_pairs_small.get('[Link DP]', '-')
        linkeffect = info_pairs_small.get('[Link Effect]', '-')

        #   5.0     Populate Card
        final_card.append(final_image_url_text)
        final_card.append(idcode)
        final_card.append(name)
        final_card.append(colors_str)
        final_card.append(rarity)
        final_card.append(ctype)
        final_card.append(level)
        final_card.append(owned)
        final_card.append(art)
        final_card.append(form)
        final_card.append(attribute)
        final_card.append(type)
        final_card.append(dp)
        final_card.append(cost)
        final_card.append(dcost1)
        final_card.append(dcost2)
        final_card.append(spdcost)
        final_card.append(spplcond)
        final_card.append(effect)
        final_card.append(ieffect)
        final_card.append(seffect)
        final_card.append(linkcond)
        final_card.append(linkdp)
        final_card.append(linkeffect)
        final_card.append(pack)

        # print(final_card)

        final_card_list.append(final_card)





# 'Link Condition'
#     'Link DP'
#     'Link Effect'

    # card_info = {
    #     'Image' = final_image_url_text,
    #     'ID Code' = card_id,
    #     'Name' = card_name,
    #     'Color' = card_color,
    #     'Rarity' = card_rarity,
    #     'Card Type' = card_type,
    #     'Level' = card_level,
    #     'Copies Owned' = card_copies,
    #     'Art Version' = card_art,
    #     'Form' = card_form,
    #     'Attribute' = card_attribute,
    #     'Digimon Type' = card_digimon_type,
    #     'DP' = card_dp,
    #     'Play Cost' = card_pcost,
    #     'Digivolution Cost 1' = card_dcost1,
    #     'Digivolution Cost 2' = card_dcost2,
    #     'Special Digivolution Condition' = card_spdcost
    #     'Special Play Condition' = card_spcond
    #     'Effect' = card_effect,
    #     'Inherited Effect' = card_inh_effect,
    #     'Security Effect' = card_sec_effect,
    #     'Link Condition'
    #     'Link DP'
    #     'Link Effect'
    #     'Notes-Pack' = card_pack
    # }

    # 5.0   Keyword Check
        info_tit = (card.find_all('dt', class_='cardInfoTit'))
        info_tit = [dt.get_text(strip=True) for dt in info_tit if dt.get_text(strip=True)]
        info_tit_small = (card.find_all('dt', class_='cardInfoTitSmall'))
        info_tit_small = [dt.get_text(strip=True) for dt in info_tit_small if dt.get_text(strip=True)]
        info_title = '/'.join(info_tit) + '/' + '/'.join(info_tit_small)

        keyword_check = info_title.split('/')
        for keyword in keyword_check :
            if keyword not in keywords:
                keywords.append(keyword)
        # print(info_title)
        # print(keyword_check)
        # print(keywords)

        # print("card added")


print(final_card_list)
