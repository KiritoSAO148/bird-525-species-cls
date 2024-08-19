import streamlit as st
from PIL import Image
from keras.preprocessing.image import load_img,img_to_array
import numpy as np
from keras.models import load_model

birds = ['DALMATIAN PELICAN', 'BLACK BREASTED PUFFBIRD', 'WATTLED CURASSOW', 'AMERICAN WIGEON', 'CARMINE BEE-EATER', 'GAMBELS QUAIL', 'UMBRELLA BIRD', 'AMERICAN KESTREL', 'AMERICAN GOLDFINCH', 'BLUE GROSBEAK', 'PALM NUT VULTURE', 'DUSKY LORY', 'AUCKLAND SHAQ', 'BLACK THROATED WARBLER', 'YELLOW CACIQUE', 'STRIPPED SWALLOW', 'VERMILION FLYCATHER', 'CAPE MAY WARBLER', 'RED TAILED HAWK', 'GURNEYS PITTA', 'INDIAN ROLLER', 'SNOW GOOSE', 'GREEN WINGED DOVE', 'AZURE TANAGER', 'GREEN MAGPIE', 'BANDED BROADBILL', 'AFRICAN PYGMY GOOSE', 'INDIGO FLYCATCHER', 'GREY PLOVER', 'TOUCHAN', 'HYACINTH MACAW', 'HARLEQUIN DUCK', 'ABYSSINIAN GROUND HORNBILL', 'CALIFORNIA QUAIL', 'BALD IBIS', 'WOOD THRUSH', 'RUBY THROATED HUMMINGBIRD', 'INDIGO BUNTING', 'ALBERTS TOWHEE', 'SORA', 'HOODED MERGANSER', 'ROSEATE SPOONBILL', 'CAPE ROCK THRUSH', 'BLUE COAU', 'CALIFORNIA CONDOR', 'BORNEAN PHEASANT', 'BARN SWALLOW', 'TAIWAN MAGPIE', 'SPLENDID WREN', 'RED BILLED TROPICBIRD', 'BLACK THROATED BUSHTIT', 'CHINESE POND HERON', 'AFRICAN EMERALD CUCKOO', 'COMMON LOON', 'COMMON POORWILL', 'ROSE BREASTED COCKATOO', 'FIORDLAND PENGUIN', 'SUPERB STARLING', 'CUBAN TODY', 'TASMANIAN HEN', 'BLACK SWAN', 'WATTLED LAPWING', 'RED NAPED TROGON', 'SUNBITTERN', 'AMERICAN PIPIT', 'OILBIRD', 'EASTERN TOWEE', 'GYRFALCON', 'BLACK SKIMMER', 'RED BEARDED BEE EATER', 'ASIAN OPENBILL STORK', 'ALBATROSS', 'WHITE EARED HUMMINGBIRD', 'EGYPTIAN GOOSE', 'MASKED LAPWING', 'LAUGHING GULL', 'AMERICAN ROBIN', 'MALABAR HORNBILL', 'OCELLATED TURKEY', 'PEREGRINE FALCON', 'SQUACCO HERON', 'CHINESE BAMBOO PARTRIDGE', 'IBISBILL', 'ROSY FACED LOVEBIRD', 'GREATOR SAGE GROUSE', 'MILITARY MACAW', 'CHATTERING LORY', 'VISAYAN HORNBILL', 'AZARAS SPINETAIL', 'RUFOUS KINGFISHER', 'LOONEY BIRDS', 'JABIRU', 'WHITE BREASTED WATERHEN', 'GREAT KISKADEE', 'GRAY KINGBIRD', 'GUINEAFOWL', 'NORTHERN MOCKINGBIRD', 'WHITE CRESTED HORNBILL', 'MALLARD DUCK', 'GILA WOODPECKER', 'BROWN HEADED COWBIRD', 'MASKED BOOBY', 'AMERICAN BITTERN', 'CALIFORNIA GULL', 'CASPIAN TERN', 'EMERALD TANAGER', 'BANDED PITA', 'AZURE JAY', 'BARRED PUFFBIRD', 'ELEGANT TROGON', 'SNOWY EGRET', 'EUROPEAN TURTLE DOVE', 'CRESTED SHRIKETIT', 'SATYR TRAGOPAN', 'GANG GANG COCKATOO', 'AMETHYST WOODSTAR', 'RED HEADED WOODPECKER', 'MIKADO  PHEASANT', 'FIRE TAILLED MYZORNIS', 'BUFFLEHEAD', 'BLUE THROATED PIPING GUAN', 'GREAT TINAMOU', 'SWINHOES PHEASANT', 'PARADISE TANAGER', 'OVENBIRD', 'GRANDALA', 'EASTERN BLUEBONNET', 'MOURNING DOVE', 'BLACK FACED SPOONBILL', 'BROWN NOODY', 'WALL CREAPER', 'ORIENTAL BAY OWL', 'DOWNY WOODPECKER', 'EMPEROR PENGUIN', 'WHITE TAILED TROPIC', 'FIERY MINIVET', 'OSPREY', 'HOUSE FINCH', 'SNOWY PLOVER', 'AMERICAN COOT', 'GOLDEN PIPIT', 'PUFFIN', 'ARARIPE MANAKIN', 'RUDY KINGFISHER', 'CABOTS TRAGOPAN', 'BLACK-CAPPED CHICKADEE', 'ABBOTTS BABBLER', 'GREEN BROADBILL', 'KAKAPO', 'RAZORBILL', 'RED LEGGED HONEYCREEPER', 'BLACK BAZA', 'ANTILLEAN EUPHONIA', 'BEARDED REEDLING', 'ORANGE BREASTED TROGON', 'BELTED KINGFISHER', 'KILLDEAR', 'PLUSH CRESTED JAY', 'HELMET VANGA', 'BAR-TAILED GODWIT', 'CRESTED OROPENDOLA', 'STRIPPED MANAKIN', 'CAPE LONGCLAW', 'CREAM COLORED WOODPECKER', 'NORTHERN BEARDLESS TYRANNULET', 'YELLOW BELLIED FLOWERPECKER', 'RED SHOULDERED HAWK', 'RED TAILED THRUSH', 'STEAMER DUCK', 'RED BELLIED PITTA', 'GRAY CATBIRD', 'GUINEA TURACO', 'RUDDY SHELDUCK', 'RED WISKERED BULBUL', 'PATAGONIAN SIERRA FINCH', 'PHILIPPINE EAGLE', 'RED FODY', 'ANHINGA', 'VEERY', 'SPOTTED WHISTLING DUCK', 'BRANDT CORMARANT', 'SPOON BILED SANDPIPER', 'VULTURINE GUINEAFOWL', 'ENGGANO MYNA', 'YELLOW BREASTED CHAT', 'GREAT XENOPS', 'SAYS PHOEBE', 'BIRD OF PARADISE', 'LILAC ROLLER', 'BAIKAL TEAL', 'CINNAMON ATTILA', 'BANANAQUIT', 'JOCOTOCO ANTPITTA', 'CHUKAR PARTRIDGE', 'CRIMSON CHAT', 'EASTERN GOLDEN WEAVER', 'CACTUS WREN', 'BALD EAGLE', 'CAPE GLOSSY STARLING', 'BURCHELLS COURSER', 'IVORY BILLED ARACARI', 'NICOBAR PIGEON', 'KIWI', 'AFRICAN FIREFINCH', 'CRESTED NUTHATCH', 'GOLD WING WARBLER', 'WHITE BROWED CRAKE', 'DUNLIN', 'COCKATOO', 'BLUE THROATED TOUCANET', 'CAATINGA CACHOLOTE', 'EMU', 'FAIRY TERN', 'HARPY EAGLE', 'ANDEAN SISKIN', 'DOUBLE EYED FIG PARROT', 'BLUE MALKOHA', 'GREAT ARGUS', 'CUBAN TROGON', 'VIOLET TURACO', 'BLONDE CRESTED WOODPECKER', 'ASHY THRUSHBIRD', 'BLUE HERON', 'EURASIAN MAGPIE', 'RED WINGED BLACKBIRD', 'ZEBRA DOVE', 'BORNEAN BRISTLEHEAD', 'FAN TAILED WIDOW', 'WRENTIT', 'COLLARED CRESCENTCHEST', 'CANVASBACK', 'FOREST WAGTAIL', 'CHESTNET BELLIED EUPHONIA', 'IBERIAN MAGPIE', 'SCARLET CROWNED FRUIT DOVE', 'ORANGE BRESTED BUNTING', 'SCARLET TANAGER', 'ASIAN DOLLARD BIRD', 'ANDEAN LAPWING', 'MAGPIE GOOSE', 'KING EIDER', 'BLACK THROATED HUET', 'WHITE THROATED BEE EATER', 'TROPICAL KINGBIRD', 'PARAKETT  AUKLET', 'BLACK FRANCOLIN', 'ASHY STORM PETREL', 'COLLARED ARACARI', 'CRESTED AUKLET', 'GLOSSY IBIS', 'NORTHERN CARDINAL', 'KAGU', 'SURF SCOTER', 'PURPLE FINCH', 'ANDEAN GOOSE', 'HORNED SUNGEM', 'MYNA', 'COMMON HOUSE MARTIN', 'EURASIAN GOLDEN ORIOLE', 'NORTHERN SHOVELER', 'AVADAVAT', 'ANTBIRD', 'PHAINOPEPLA', 'POMARINE JAEGER', 'BLUE GRAY GNATCATCHER', 'CLARKS GREBE', 'APOSTLEBIRD', 'COPPERY TAILED COUCAL', 'ALEXANDRINE PARAKEET', 'MCKAYS BUNTING', 'CEDAR WAXWING', 'KING VULTURE', 'SAND MARTIN', 'SMITHS LONGSPUR', 'ALPINE CHOUGH', 'PYGMY KINGFISHER', 'GOULDIAN FINCH', 'CRESTED WOOD PARTRIDGE', 'CROW', 'RED KNOT', 'BROWN CREPPER', 'TAWNY FROGMOUTH', 'NOISY FRIARBIRD', 'CERULEAN WARBLER', 'CAMPO FLICKER', 'WHITE CHEEKED TURACO', 'BARN OWL', 'STRIPED OWL', 'TAILORBIRD', 'VIOLET BACKED STARLING', 'IVORY GULL', 'OSTRICH', 'ROUGH LEG BUZZARD', 'RAINBOW LORIKEET', 'BAND TAILED GUAN', 'APAPANE', 'HIMALAYAN BLUETAIL', 'PARUS MAJOR', 'LONG-EARED OWL', 'CRESTED FIREBACK', 'EASTERN YELLOW ROBIN', 'MARABOU STORK', 'EURASIAN BULLFINCH', 'BLACK TAIL CRAKE', 'GOLDEN BOWER BIRD', 'INCA TERN', 'PAINTED BUNTING', 'EASTERN BLUEBIRD', 'PALILA', 'HOOPOES', 'OKINAWA RAIL', 'AUSTRALASIAN FIGBIRD', 'CHIPPING SPARROW', 'TRICOLORED BLACKBIRD', 'AMERICAN FLAMINGO', 'WILLOW PTARMIGAN', 'ANNAS HUMMINGBIRD', 'CINNAMON TEAL', 'SCARLET FACED LIOCICHLA', 'WOODLAND KINGFISHER', 'VENEZUELIAN TROUPIAL', 'HEPATIC TANAGER', 'MALEO', 'IWI', 'WHITE NECKED RAVEN', 'PINK ROBIN', 'BOBOLINK', 'MANDRIN DUCK', 'RED BROWED FINCH', 'PYRRHULOXIA', 'NORTHERN PARULA', 'COPPERSMITH BARBET', 'AMERICAN AVOCET', 'EVENING GROSBEAK', 'RED HEADED DUCK', 'TREE SWALLOW', 'COMMON GRACKLE', 'SCARLET MACAW', 'HORNED GUAN', 'CHESTNUT WINGED CUCKOO', 'BLACK VENTED SHEARWATER', 'RED CROSSBILL', 'CAPUCHINBIRD', 'MANGROVE CUCKOO', 'CRAB PLOVER', 'CINNAMON FLYCATCHER', 'WILD TURKEY', 'DUSKY ROBIN', 'VIOLET GREEN SWALLOW', 'AUSTRAL CANASTERO', 'BUSH TURKEY', 'GOLDEN PARAKEET', 'LESSER ADJUTANT', 'GREEN JAY', 'ALTAMIRA YELLOWTHROAT', 'FRILL BACK PIGEON', 'BEARDED BELLBIRD', 'FLAME BOWERBIRD', 'PUNA TEAL', 'LIMPKIN', 'RUFUOS MOTMOT', 'CRESTED KINGFISHER', 'NORTHERN JACANA', 'ECUADORIAN HILLSTAR', 'ROADRUNNER', 'BLUE GROUSE', 'CAPPED HERON', 'TEAL DUCK', 'DARK EYED JUNCO', 'LOGGERHEAD SHRIKE', 'CLARKS NUTCRACKER', 'GILDED FLICKER', 'CHUCAO TAPACULO', 'BALI STARLING', 'SNOW PARTRIDGE', 'GREY CUCKOOSHRIKE', 'VERDIN', 'GREAT GRAY OWL', 'ROCK DOVE', 'BREWERS BLACKBIRD', 'LUCIFER HUMMINGBIRD', 'BLOOD PHEASANT', 'ORNATE HAWK EAGLE', 'AFRICAN PIED HORNBILL', 'CHARA DE COLLAR', 'TOWNSENDS WARBLER', 'D-ARNAUDS BARBET', 'MERLIN', 'OYSTER CATCHER', 'VARIED THRUSH', 'RUFOUS TREPE', 'SRI LANKA BLUE MAGPIE', 'SNOWY SHEATHBILL', 'LARK BUNTING', 'DOUBLE BARRED FINCH', 'FAIRY BLUEBIRD', 'CRIMSON SUNBIRD', 'HARLEQUIN QUAIL', 'HOUSE SPARROW', 'AMERICAN DIPPER', 'CRESTED CARACARA', 'NORTHERN GANNET', 'SCARLET IBIS', 'MALACHITE KINGFISHER', 'INDIAN PITTA', 'EASTERN MEADOWLARK', 'REGENT BOWERBIRD', 'WILSONS BIRD OF PARADISE', 'COMMON IORA', 'BLACK NECKED STILT', 'SHORT BILLED DOWITCHER', 'BLACK-THROATED SPARROW', 'DARJEELING WOODPECKER', 'NORTHERN FLICKER', 'BANDED STILT', 'GREY HEADED CHACHALACA', 'PURPLE GALLINULE', 'CANARY', 'TAKAHE', 'JANDAYA PARAKEET', 'FLAME TANAGER', 'CURL CRESTED ARACURI', 'FASCIATED WREN', 'GREATER PEWEE', 'RED FACED CORMORANT', 'GREAT JACAMAR', 'ROSE BREASTED GROSBEAK', 'ROYAL FLYCATCHER', 'NORTHERN FULMAR', 'EARED PITA', 'BULWERS PHEASANT', 'HORNED LARK', 'HAWFINCH', 'COCK OF THE  ROCK', 'TIT MOUSE', 'GRAY PARTRIDGE', 'AZURE BREASTED PITTA', 'ANIANIAU', 'WOOD DUCK', 'KNOB BILLED DUCK', 'GROVED BILLED ANI', 'RED FACED WARBLER', 'HIMALAYAN MONAL', 'DEMOISELLE CRANE', 'CRESTED COUA', 'QUETZAL', 'NORTHERN GOSHAWK', 'GOLDEN CHLOROPHONIA', 'RUBY CROWNED KINGLET', 'PURPLE SWAMPHEN', 'COMMON FIRECREST', 'TURQUOISE MOTMOT', 'CASSOWARY', 'INDIAN BUSTARD', 'KOOKABURRA', 'SANDHILL CRANE', 'RING-NECKED PHEASANT', 'MASKED BOBWHITE', 'EASTERN ROSELLA', 'GREY HEADED FISH EAGLE', 'PURPLE MARTIN', 'VICTORIA CROWNED PIGEON', 'SHOEBILL', 'SNOWY OWL', 'AFRICAN CROWNED CRANE', 'GREAT POTOO', 'STORK BILLED KINGFISHER', 'BLACK HEADED CAIQUE', 'GOLDEN PHEASANT', 'AFRICAN OYSTER CATCHER', 'ASIAN CRESTED IBIS', 'EASTERN WIP POOR WILL', 'LITTLE AUK', 'BLACK-NECKED GREBE', 'ABBOTTS BOOBY', 'BALTIMORE ORIOLE', 'VIOLET CUCKOO', 'COMMON STARLING', 'HAMERKOP', 'INDIAN VULTURE', 'JAPANESE ROBIN', 'BLACKBURNIAM WARBLER', 'WHIMBREL', 'YELLOW HEADED BLACKBIRD', 'SPOTTED CATBIRD', 'BLACK COCKATO', 'SPANGLED COTINGA', 'FAIRY PENGUIN', 'MALAGASY WHITE EYE', 'HAWAIIAN GOOSE', 'PEACOCK', 'BEARDED BARBET', 'TURKEY VULTURE', 'JACK SNIPE', 'ASIAN GREEN BEE EATER', 'BLACK VULTURE', 'BROWN THRASHER', 'BLUE DACNIS', 'DAURIAN REDSTART', 'STRIATED CARACARA', 'GREATER PRAIRIE CHICKEN', 'GOLDEN CHEEKED WARBLER', 'DOUBLE BRESTED CORMARANT', 'JAVA SPARROW', 'BAY-BREASTED WARBLER', 'AZURE TIT', 'HOATZIN', 'GO AWAY BIRD', 'ELLIOTS  PHEASANT', 'JACOBIN PIGEON', 'CRESTED SERPENT EAGLE', 'IMPERIAL SHAQ', 'BARROWS GOLDENEYE', 'FRIGATE', 'TRUMPTER SWAN', 'INLAND DOTTEREL', 'SAMATRAN THRUSH', 'BLACK AND YELLOW BROADBILL', 'BORNEAN LEAFBIRD', 'LAZULI BUNTING', 'EUROPEAN GOLDFINCH', 'AMERICAN REDSTART', 'CRANE HAWK', 'NORTHERN RED BISHOP', 'GOLDEN EAGLE']
birds.sort()
lab = {index: bird for index, bird in enumerate(birds)}
# print(lab)

model = load_model('./BC.h5', compile=False)

def processed_img(img_path):
    img=load_img(img_path,target_size=(224,224,3))
    img=img_to_array(img)
    img=img/255
    img=np.expand_dims(img,[0])
    answer=model.predict(img)
    y_class = answer.argmax(axis=-1)
    print(y_class)
    y = " ".join(str(x) for x in y_class)
    y = int(y)
    res = lab[y]
    print(res)
    return res

def run():
    img1 = Image.open('./meta/logo1.png')
    img1 = img1.resize((350,350))
    st.image(img1,use_column_width=False)
    st.title("Birds Species Classification")
    st.markdown('''<h4 style='text-align: left; color: #d73b5c;'>* Data is based "270 Bird Species also see 70 Sports Dataset"</h4>''',
                unsafe_allow_html=True)

    img_file = st.file_uploader("Choose an Image of Bird", type=["jpg", "png"])
    if img_file is not None:
        st.image(img_file,use_column_width=False)
        save_image_path = './upload_images/'+img_file.name
        with open(save_image_path, "wb") as f:
            f.write(img_file.getbuffer())

        if st.button("Predict"):
            result = processed_img(save_image_path)
            st.success("Predicted Bird is: "+result)
run()