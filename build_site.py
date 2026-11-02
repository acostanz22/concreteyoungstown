# -*- coding: utf-8 -*-
"""Generate the static Youngstown Concrete Contractors site."""
import html
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent
PHONE_DISP = "(330) 293-2914"
PHONE_TEL = "+13302932914"
SITE = "https://www.concreteyoungstown.net"
BRAND = "Youngstown Concrete Contractors"
SOURCE = "Youngstown%20Concrete%20Contractors"
TALLY = (
    "https://tally.so/embed/xX6B0y?alignLeft=1&hideTitle=1"
    "&transparentBackground=1&dynamicHeight=1&source=" + SOURCE
)

def e(text):
    return html.escape(text, quote=True)

from _svc_data import SERVICES

LOCATIONS = [
    {
        "href": "boardman.html",
        "name": "Boardman",
        "title": "Concrete in Boardman, OH | Youngstown Concrete Contractors",
        "desc": "Concrete driveways, patios, and flatwork in Boardman, Ohio. Slope, salt, and longer suburban drives planned on site. Call (330) 293-2914.",
        "h1": "Concrete Contractors in Boardman, Ohio",
        "intro": "Boardman sits directly south of Youngstown, with longer residential drives and commercial frontage along Route 224. The concrete work is the same valley climate: freeze-thaw, road salt, and soils that hold water. What changes is the lot. Subdivision drives are often longer than a city lot in Youngstown, and a patio behind the house has to share the yard with drainage from a larger roof.",
        "detail": "We replace scaled driveways, pour patios that fall away from the foundation, and patch or replace aprons that have broken at the street. A Boardman drive that slopes back toward the garage is a layout problem, not a sealing problem. We measure that fall before we talk about broom finish or stamp.",
        "jobs": [
            ("concrete-driveways.html", "Driveway replacement", "Longer drives where salt has scaled the surface or the center has settled."),
            ("concrete-patios.html", "Patios", "Backyard slabs for houses off the 224 corridor and in the subdivisions, with slope set away from the wall."),
            ("stamped-concrete.html", "Stamped flatwork", "Front walks and patios when a plain broom finish is not the look you want on a new pour."),
        ],
        "faqs": [
            ("Can you replace a long Boardman driveway that slopes toward the garage?", "Yes. The new grade has to leave the garage and still meet the sidewalk or the street. On a long drive that sometimes means correcting a belly in the middle, not just raising the garage end. We will show you the fall before we form it."),
            ("Do you pour patios behind houses in the Boardman subdivisions?", "Yes. We lay the patio out against the door, the yard drainage, and whatever you need to keep, including basement windows. A larger suburban yard does not change the rule that water has to move away from the house."),
            ("How do you get concrete into a Boardman backyard with a narrow side gate?", "If the truck can reach the street side, we buggy the concrete through the gate when the opening is wide enough. If it is not, we say so and price the access we actually have. A gate that looks wide enough for a mower is often tight for a loaded buggy."),
            ("Is asphalt or concrete more practical on a Boardman driveway?", "Both are on the table. Concrete is the usual replacement when the old slab has scaled and you want a rigid drive. Asphalt fits some lots where a flexible surface and a faster return to parking matter more. We will tell you which one the base and the slope support."),
        ],
    },
    {
        "href": "austintown.html",
        "name": "Austintown",
        "title": "Concrete in Austintown, OH | Youngstown Concrete Contractors",
        "desc": "Driveways, aprons, and small pads in Austintown, Ohio. Concrete work for ranch lots and Mahoning Avenue frontage. Call (330) 293-2914.",
        "h1": "Concrete Contractors in Austintown, Ohio",
        "intro": "Austintown is west of Youngstown, a mix of ranch-house streets and commercial lots along Mahoning Avenue. Driveways here take salt from a busy township, and many of the slabs are original to mid-century houses. The failure we see most is a cracked apron at the street and a drive that has settled out of plane with the garage.",
        "detail": "We also pour small parking pads and walkways for shops and houses on the corridor, where the work has to meet an existing sidewalk and leave a usable entrance. Tight side yards are common. Access is part of the estimate, not a surprise on pour day.",
        "jobs": [
            ("concrete-driveways.html", "Driveways and aprons", "Replacements where the street end has broken up and the garage end no longer meets the floor."),
            ("concrete-installation.html", "Pads and walks", "Equipment pads, short walks, and parking pads that tie into an existing drive."),
            ("asphalt-paving.html", "Asphalt", "Small lots where a flexible pavement is the better surface and the base can support it."),
        ],
        "faqs": [
            ("Can you replace a cracked apron on a busy Austintown street?", "Yes, when the apron is private work and we can form it to the sidewalk and the gutter. We keep a path for cars that still need the street, and we will tell you if the public walk next to the apron is a city repair rather than part of our pour."),
            ("Do you pour small parking pads along Mahoning Avenue?", "Yes. A pad for a shop or a house still needs thickness for the vehicles that will use it, and it has to drain without sending water at the building or across the sidewalk in a sheet. Tell us what parks there."),
            ("What if the old drive sits higher than the sidewalk?", "We cut the replacement down to a slope that meets the walk without a bump or a pond. Building the new drive on top of a high slab usually makes the garage and the sidewalk worse. Removal is the normal path."),
            ("Can you work if a car has to stay until pour day?", "Yes. Tell us that when we measure. We plan the breakout and the pour so you are not blocked longer than the work requires. Once the new concrete is down, the car stays off it until it can take the weight."),
        ],
    },
    {
        "href": "canfield.html",
        "name": "Canfield",
        "title": "Concrete in Canfield, OH | Youngstown Concrete Contractors",
        "desc": "Concrete driveways and patios in Canfield, Ohio, including sloped lots and stamped flatwork. Call (330) 293-2914 for a site estimate.",
        "h1": "Concrete Contractors in Canfield, Ohio",
        "intro": "Canfield is southwest of Youngstown, with village streets and larger township lots. Driveways run longer, and more of the calls are patios and decorative walks rather than a short city apron. The winter is the same. A stamped patio still has to sit on a real base, and a drive on a grade still has to keep water out of a walkout basement.",
        "detail": "We look at the fall from the house to the yard before we choose a finish. A pretty stamp on a slab that pitches the wrong way is a problem you will see every rain. Steps, door landings, and a walk to the drive are often part of the same pour.",
        "jobs": [
            ("stamped-concrete.html", "Stamped patios and walks", "New decorative flatwork where the pattern is chosen before the pour, not added later."),
            ("concrete-patios.html", "Patios on a grade", "Slabs that step or slope with the yard and still fall away from the house."),
            ("concrete-driveways.html", "Longer driveways", "Replacements where length, thickness, and drainage change the estimate more than the finish."),
        ],
        "faqs": [
            ("Do larger Canfield lots change the driveway estimate?", "Yes. More square footage, a longer carry from the truck, and sometimes more base where the soil is soft. A longer drive is not priced as a short city apron with extra zeros. We measure it."),
            ("Can you stamp a patio where the yard drops away from the house?", "Yes, if we can form a stable slab or a simple step without fighting the grade. A stamp does not fix a hillside. If the drop is too much for a single slab, we will say the patio needs to be smaller or stepped."),
            ("Will you tie a new walk into an existing front step?", "Yes. We set the walk to the step you are keeping, with a joint at the meeting point. If the step itself is tipped or the landing holds water, we will tell you the step should be replaced with the walk."),
            ("How do you keep water off a walkout basement?", "The patio and the adjacent grade have to fall away from the wall, and downspouts cannot dump into that same corner. If the yard is flat against the walkout, concrete alone will not dry it out. We include the slope in the layout."),
        ],
    },
    {
        "href": "poland.html",
        "name": "Poland",
        "title": "Concrete in Poland, OH | Youngstown Concrete Contractors",
        "desc": "Concrete driveways, sidewalks, and patios in Poland, Ohio. Village access and sloped yards handled on site. Call (330) 293-2914.",
        "h1": "Concrete Contractors in Poland, Ohio",
        "intro": "Poland is southeast of Youngstown. Village streets can be tight for a concrete truck, and township properties outside the village often have more grade and a longer approach. The work is driveways, private walks, and patios that deal with freeze-thaw and with water moving across a sloped yard.",
        "detail": "We plan truck access before pour day. A village drive with limited swing room may be placed by buggy from the street. On a sloped township lot, the first question is where the water goes after it leaves the slab, not which broom or stamp you like.",
        "jobs": [
            ("concrete-driveways.html", "Village and township drives", "Replacements sized to the street width and the garage you already have."),
            ("concrete-installation.html", "Sidewalk panels", "Private walk replacement where a single heaved square is a trip edge."),
            ("concrete-patios.html", "Patios", "Backyard slabs that follow the grade instead of damming it against the house."),
        ],
        "faqs": [
            ("Can a concrete truck reach a Poland village driveway?", "Sometimes it can, and sometimes we stage on the street and move the concrete in. We check the width, the overhead lines, and the parked cars before we promise a truck in the drive. Access is written into the estimate."),
            ("Do you replace sidewalk squares that have heaved?", "Yes, on private walks, and on the portion of a front walk that is yours. One lifted square can be cut out and repoured if its neighbors are stable. If the whole run has moved, one square will not level the path."),
            ("What finish holds up on a Poland driveway that sees road salt?", "A broom finish on air-entrained concrete, with joints and a real base, is the durable everyday choice. Salt will still mark a surface over the years. A decorative stamp is optional, and it needs a texture you can shovel. We will not sell a sealer as protection from winter."),
            ("Can you add a patio without blocking a basement window?", "Yes. We keep the slab and the grade below an egress opening and out of the window well. If a patio design would cover that well, we change the layout. A bigger slab is not worth a blocked exit."),
        ],
    },
    {
        "href": "struthers.html",
        "name": "Struthers",
        "title": "Concrete in Struthers, OH | Youngstown Concrete Contractors",
        "desc": "Concrete driveway and apron replacement in Struthers, Ohio, including tight lots where the truck stays on the street. Call (330) 293-2914.",
        "h1": "Concrete Contractors in Struthers, Ohio",
        "intro": "Struthers is east of Youngstown, with older houses and shorter driveways. Many pours are garage aprons, narrow drives, and private walks where a truck cannot pull in. Freeze-thaw and salt do the same damage here as on a wider suburban drive. The difference is room: forms, breakout, and the concrete itself often move through a tight side yard.",
        "detail": "We would rather buggy a short drive from the street than tear up a yard pretending the truck will fit. If only the apron has failed, we can replace that section and leave a sound driveway. If the whole slab has scaled, a partial pour will not hide it.",
        "jobs": [
            ("concrete-driveways.html", "Short driveways", "Full replacements where the slab has scaled or settled toward the garage."),
            ("concrete-installation.html", "Aprons and walks", "The street-end apron or a heaved walk, when the rest of the concrete can stay."),
            ("stained-concrete.html", "Stain on a sound slab", "Color for a patio or porch slab that is still solid. Not a cover for scaling."),
        ],
        "faqs": [
            ("Can you replace a short Struthers driveway if the truck cannot pull in?", "Yes. We break out the old slab, haul it, and place the new concrete from the street when that is the access you have. The estimate includes that carry. A short drive is not automatically a small job if everything has to be wheeled."),
            ("Do you pour garage aprons separately from the rest of the drive?", "Yes, when the driveway above the apron is sound and at the right height. We dowel the new apron to the drive and set the slope so water is not trapped at the door or dumped across the sidewalk."),
            ("What if the sidewalk at the street belongs to the city?", "Then our pour stops at your apron or your private walk. We will point out the line. Rebuilding a public sidewalk the city is responsible for is not part of a driveway replacement unless you have been told it is your repair."),
            ("Is a 4-inch slab enough for a passenger car in Struthers?", "Usually, over a compacted base, for cars. If you park a heavier truck, or the soil is soft and wet, we thicken the section. The street being narrow does not change the thickness the vehicle needs."),
        ],
    },
    {
        "href": "warren.html",
        "name": "Warren",
        "title": "Concrete in Warren, OH | Youngstown Concrete Contractors",
        "desc": "Concrete and asphalt flatwork in Warren, Ohio. Driveways, patios, and small pads for the same winters as Youngstown. Call (330) 293-2914.",
        "h1": "Concrete Contractors in Warren, Ohio",
        "intro": "Warren is north of Youngstown in Trumbull County, close enough that we treat it as part of the regular service area. Winters match the valley: repeated freeze-thaw and salt on streets that never fully dry. We pour and replace driveways, patios, sidewalks, and small pads for houses and for lots that are not highway work.",
        "detail": "A Warren driveway does not get a different product with the city name swapped on it. The visit is about your slab, your garage height, and your base. If the job is asphalt that has alligatored, we will say whether a patch, a new mat, or a switch to concrete fits the failure.",
        "jobs": [
            ("concrete-driveways.html", "Concrete driveways", "Replacements for scaled and cracked drives on city and neighborhood lots."),
            ("asphalt-paving.html", "Asphalt drives", "Repaving where the surface has failed and a flexible pavement still fits."),
            ("concrete-patios.html", "Patios", "Backyard slabs sloped away from older foundations that do not need extra water."),
        ],
        "faqs": [
            ("Do you take driveway and patio work in Warren, or only in Youngstown?", "We work in Warren. It is part of the area we schedule with Youngstown, Boardman, Niles, and the other towns on the service area page. Call with the address. If the lot is farther than we cover that week, we will say so."),
            ("Can you replace failed asphalt with concrete in Warren?", "Yes, if the base is rebuilt for a rigid slab and the height still works at the garage and the sidewalk. Switching materials without fixing a soft base just gives you a cracked concrete drive. We look at what is under the asphalt first."),
            ("How do Warren winters change the pour?", "We plan joints, drainage, and an air-entrained mix suited to freeze-thaw, and we will not pour if the temperature will not let the concrete set. Salt is still going to reach the surface. The pour is built for that exposure. It is not waterproofed against it."),
            ("Do you pour commercial pads as well as house driveways?", "Small pads, aprons, and parking areas for a shop or a lot, yes. We are not bidding road reconstruction or building foundations. If the job is flatwork you can walk, we can usually price it after a look."),
        ],
    },
    {
        "href": "niles.html",
        "name": "Niles",
        "title": "Concrete in Niles, OH | Youngstown Concrete Contractors",
        "desc": "Concrete driveway replacement and patios in Niles, Ohio. Garage height, removal, and cure time set on site. Call (330) 293-2914.",
        "h1": "Concrete Contractors in Niles, Ohio",
        "intro": "Niles sits between Youngstown and Warren. The driveways are a mix of older concrete and asphalt on city lots, with the same salt and frost heave as the rest of the metro. Most replacement jobs start with one question: does the slab come out, or is any of it sound enough to keep?",
        "detail": "We check the garage floor, the sidewalk, and the drainage before we answer that. A new drive that is too high at the door, or poured over a slab that is still moving, will crack in the old pattern. Stain is only a topic if the patio you want colored is still solid.",
        "jobs": [
            ("concrete-driveways.html", "Driveway replacement", "Tear-out and new concrete matched to the garage and the street."),
            ("concrete-patios.html", "Patios", "New slabs where the yard is mud or the old patio has become a trip hazard."),
            ("stained-concrete.html", "Stain, when it fits", "Color on concrete that has not scaled or settled. We will decline it when the slab has failed."),
        ],
        "faqs": [
            ("Can you match a new Niles driveway to the garage floor?", "Yes. Meeting the garage without a lip, and still draining away from it, is part of the layout. If an old overlay built the drive up too high, we remove that and start from a height that works."),
            ("Do you remove the failed slab, or pour over it?", "We remove it when it is cracked through, rocking, or holding water. Pouring over that kind of slab is a short-lived cover. A panel that is solid and at the right elevation can sometimes stay and be tied to the new concrete."),
            ("Is stained concrete worth it on a Niles patio that already has cracks?", "Only if the cracks are tight joints and the slab is stable. Stain will not glue a separated patio back together, and it will darken every patch. If you are unsure, ask us to look before you pick a color."),
            ("How soon can we park on a new driveway?", "Several days for a car, longer when nights are cold. We set the day from the pour and the forecast before we leave Niles. Walking on it happens sooner than parking on it."),
        ],
    },
    {
        "href": "girard.html",
        "name": "Girard",
        "title": "Concrete in Girard, OH | Youngstown Concrete Contractors",
        "desc": "Concrete driveways, walks, and small pads in Girard, Ohio. Tight side yards and salt-damaged edges. Call (330) 293-2914.",
        "h1": "Concrete Contractors in Girard, Ohio",
        "intro": "Girard is a small city just north of Youngstown, between the city and Niles. Lots are often modest, drives are short, and the edges of older slabs crumble where salt and plows hit them. We replace drives, pour walks to detached garages, and put in pads where a side yard is the only way to move material.",
        "detail": "Crumbling edges are usually a base and a joint problem, sometimes with too little thickness at the unsupported side. Filling the edge with a skim will not hold. We cut back to sound concrete or replace the panel, then form an edge that has stone under it.",
        "jobs": [
            ("concrete-driveways.html", "Driveway panels", "Full replacements, or the broken bays only, when the rest of the drive is stable."),
            ("concrete-installation.html", "Walks and pads", "A walk to a detached garage, or a pad that has to fit a narrow side yard."),
            ("asphalt-paving.html", "Asphalt", "Small drives where the existing asphalt has failed and a new mat is the right fix."),
        ],
        "faqs": [
            ("Can you get forms and concrete into a tight Girard side yard?", "If a wheelbarrow fits, we can usually buggy concrete through. If the opening is narrower than that, or a fence has to come down, we will say so before you schedule a pour. Access changes the price more than the finish does."),
            ("Do you replace only the broken panels of a driveway?", "Yes, when the other panels are solid, level enough, and worth keeping. We cut at the joints and dowel into the sound concrete. If every bay is cracked, replacing one leaves you with a new square in a failed drive."),
            ("What causes the edges of a Girard driveway to crumble?", "Salt, freeze-thaw, and an edge with little base under it. Plows and tires finish the job. The repair is a new edge or a new panel with stone underneath, not a surface coat on loose concrete."),
            ("Can you pour a walk from the back door to a detached garage?", "Yes. We slope it so it is not a river between the two buildings, and we joint it where it meets the existing slabs. Tell us if you need it wide enough for a mower, not only for a person."),
        ],
    },
    {
        "href": "hubbard.html",
        "name": "Hubbard",
        "title": "Concrete in Hubbard, OH | Youngstown Concrete Contractors",
        "desc": "Concrete driveways and patios in Hubbard, Ohio. Clay soils, drainage, and freeze-thaw built into the pour. Call (330) 293-2914.",
        "h1": "Concrete Contractors in Hubbard, Ohio",
        "intro": "Hubbard is east of Youngstown, toward the Pennsylvania line. Residential drives and patios here sit on the clay soils typical of this side of the valley. Clay holds water, and a slab poured on wet, unprepared ground will move. The work is ordinary and specific: compact a base, slope the surface, and joint the concrete so winter has a place to crack it straight.",
        "detail": "Downspouts matter in Hubbard as much as the concrete. A patio at the back door will stay wet if a spout dumps beside it. We look at that, and at whether you want one plan for a broom-finish drive and a stamped walk, before we schedule a truck.",
        "jobs": [
            ("concrete-driveways.html", "Driveways on clay", "Replacements with a stone base so the slab is not sitting in soft soil."),
            ("concrete-patios.html", "Patios", "Backyard slabs tied to downspout and yard drainage, not poured in a low spot."),
            ("stamped-concrete.html", "Stamped walks", "A decorative walk with a broom-finished drive, planned as one layout."),
        ],
        "faqs": [
            ("Do you serve Hubbard, toward the Pennsylvania line?", "Yes. Hubbard is on our service area list with Youngstown and the nearby townships. If your address is past Hubbard and you are unsure, call and we will tell you whether we can schedule it."),
            ("How should a Hubbard driveway be sloped on a clay lot?", "Away from the garage and off the slab, into a yard or the street that can take the water. Clay will not soak up a puddle the way sandy ground might. If the yard has nowhere for that water to go, we talk about grade before we pour."),
            ("Can you stamp a front walk and broom-finish the drive in one plan?", "Yes. They can be poured together or staged, with a joint between the decorative walk and the drive. The stamp has to happen while that section is fresh. We will not try to stamp the drive later because the walk turned out well."),
            ("What should I do about downspouts before a patio pour?", "Point them somewhere other than the new slab or the foundation. Extensions that dump at the edge of the patio will stain it and keep the base wet. We will flag a spout that is going to fight the pour."),
        ],
    },
    {
        "href": "campbell.html",
        "name": "Campbell",
        "title": "Concrete in Campbell, OH | Youngstown Concrete Contractors",
        "desc": "Concrete driveway, apron, and shed-pad work in Campbell, Ohio. Narrow lots and salt-scaled slabs. Call (330) 293-2914.",
        "h1": "Concrete Contractors in Campbell, Ohio",
        "intro": "Campbell is on Youngstown’s southeast side, with older houses on smaller lots. Driveways are narrow, staging room is limited, and a lot of the concrete has reached the end of a hard life with salt and frost. We replace drives, pour shed pads, and reset aprons. We do not turn the visit into a story about the town. The question is whether the truck stays on the street and how much of the slab is still sound.",
        "detail": "Scaling, where the surface paste flakes and the stone shows, is different from a crack that is doing the job of a joint. Scale on a driving surface usually means the top is gone and a coating will not bring it back. A straight joint crack in a stable slab may not need a replacement at all.",
        "jobs": [
            ("concrete-driveways.html", "Narrow driveways", "Full replacements when the surface has scaled or the slabs have settled."),
            ("concrete-installation.html", "Shed pads and aprons", "Small pads and street aprons where access is the hard part of the job."),
            ("concrete-patios.html", "Small patios", "A usable slab at the back door without covering the whole yard."),
        ],
        "faqs": [
            ("Can you replace a narrow Campbell driveway with little room to stage?", "Yes. Debris and concrete often move from the street by hand or buggy. We look at the fence, the neighbor’s clearance, and where a dump trailer can sit. That plan is part of the price."),
            ("Do you repair city sidewalks, or only the private drive?", "The public sidewalk is often the city’s. We pour the private drive and apron up to that line. If you have been told the walk square is your responsibility, we can price that square. We will not assume the whole front walk is part of a driveway job."),
            ("What is the difference between scaling and a crack that can stay?", "Scaling is the surface flaking away, usually from salt and freeze-thaw. A joint crack that stays tight and level can be left alone. A crack that has opened, offset, or started to break the slab into rocking pieces is a replacement conversation."),
            ("Can you pour a pad for a shed on a small Campbell lot?", "Yes. We size it to the shed and to the door swing you need, and we put it on a compacted base even when the pad is small. A thin slab on topsoil will tip when the shed is loaded. Tell us the shed dimensions when you call."),
        ],
    },
]

HOME_FAQS = [
    ("How much does a new concrete driveway cost in Youngstown?",
     "There is no honest flat price, because the number moves with square footage, thickness, removal, truck access, and the finish. A broom-finish replacement on a flat lot is a different job from a stamped patio with steps and a rebuilt base. We measure the property and send a written estimate. A photo is enough to start the conversation. It is not enough to price the work."),
    ("Can you replace a driveway broken up by freeze-thaw and salt?",
     "Yes. That is the usual driveway call around Youngstown. Salt and freeze-thaw scale the surface and open cracks until the slab is loose underfoot. If it is pitted down to the stone, rocking, or heaving, replacement outlasts a skim coat. We look at the base and the drainage before we recommend a full tear-out."),
    ("Do you offer stamped and stained concrete, or only gray broom finishes?",
     "We do both, plus plain broom-finish flatwork. Broom finish is the right driveway surface for most houses. Stamped patterns and stains are for patios, walks, and the occasional drive when you want color or the look of stone. The pattern has to be chosen before the pour. Stain is only for a slab that is still sound."),
    ("Do I need to remove the old concrete before you pour?",
     "Usually, yes, if the slab is cracked through, settled, or too high to meet the garage or the sidewalk. A thin layer over a moving slab cracks along the old lines. If one panel is still solid and at the right height, we can sometimes leave it and tie the new concrete to it. We make that call on the lot, not over the phone."),
    ("Can you do patios, sidewalks, and small pads, or only driveways?",
     "Driveways are common, and we also pour patios, private walks, aprons, and small pads for houses and businesses around Youngstown. A shed pad and a parking pad are everyday work. Road rebuilding and building foundations are not. If you can describe the flatwork, we can tell you quickly whether it is in scope."),
]

MORE_FAQS = [
    ("How soon can I drive on new concrete?",
     "Plan on several days for a passenger car, and longer when nights are near freezing. Foot traffic comes first. Asphalt is often ready sooner, once the mat has cooled. We set the actual wait for your pour before we leave, because a date promised in January does not match a pour in July."),
    ("Should I pick concrete or asphalt?",
     "Concrete stays rigid, takes a broom or a stamp, and wants joints and a stable base. Asphalt flexes, paves quickly, and still needs slope because it does not drain through the mat. Neither one fixes a yard that ponds if the grade is wrong. If the lot could go either way, we will walk it with you."),
    ("Which towns do you actually come to?",
     "Youngstown and the nearby communities listed on the service area page, including Boardman, Austintown, Canfield, Poland, Struthers, Campbell, Girard, Niles, Hubbard, and Warren. If your town is not on that list, call anyway. We would rather tell you yes or no than have you guess from a map."),
    ("What should I have ready when you come look?",
     "The address, a sense of whether this is a replacement or a new slab, and what will drive or sit on it. If a car, a fence, or a dumpster is in the way, leave access to the edge of the concrete. You do not need a drawing. You do need to be able to show us the low spot and the door the patio has to meet."),
]


def words(text):
    return len(text.split())


def tally_block():
    return f"""<div class="form-card" id="quote">
      <h2>Get a free quote</h2>
      <iframe data-tally-src="{TALLY}" loading="lazy" width="100%" height="552" frameborder="0" marginheight="0" marginwidth="0" title="Get a free quote"></iframe>
    </div>"""


def page_hero(crumbs, h1, paras, bg, actions=None, eyebrow=None, extra_class=""):
    """Page hero with copy on the left and the quote form (id="quote") on the right."""
    if actions is None:
        actions = f'<a class="btn btn-red" href="tel:{PHONE_TEL}">Call {PHONE_DISP}</a>'
    eyebrow_html = f'<p class="eyebrow">{e(eyebrow)}</p>' if eyebrow else ""
    paras_html = "".join(
        f'<p class="lede">{p}</p>' if i == 0 else f"<p>{p}</p>" for i, p in enumerate(paras)
    )
    return f"""<section class="page-hero hero-with-form {extra_class}" style="--hero: url('{bg}')">
  <div class="wrap hero-grid">
    <div class="hero-copy">
      {crumbs}
      {eyebrow_html}
      <h1>{h1}</h1>
      {paras_html}
      <div class="hero-actions">{actions}</div>
    </div>
    {tally_block()}
  </div>
</section>"""


def cta_band(title, text):
    return f"""<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="cta-band">
      <div>
        <h2>{e(title)}</h2>
        <p>{e(text)}</p>
      </div>
      <div class="hero-actions">
        <a class="btn btn-red" href="tel:{PHONE_TEL}">Call {PHONE_DISP}</a>
        <a class="btn btn-ghost" href="#quote">Request an estimate</a>
      </div>
    </div>
  </div>
</section>"""


def faq_html(items):
    parts = ['<div class="faq">']
    for q, a in items:
        parts.append(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>")
    parts.append("</div>")
    return "\n".join(parts)


def nav(current):
    service_links = ['<a href="services-850767-875359.html">All services</a>']
    for s in SERVICES:
        service_links.append(f'<a href="{s["href"]}">{e(s["name"])}</a>')
    links = [
        ("services-850767-875359.html", "Services", True),
        ("service-areas.html", "Service Areas", False),
        ("about.html", "About", False),
        ("faq.html", "FAQs", False),
        ("contact.html", "Contact", False),
    ]
    out = ['<nav class="nav" id="site-nav" aria-label="Primary">']
    out.append('<div class="nav-drop">')
    out.append('<button type="button" aria-haspopup="true">Services</button>')
    out.append('<a class="nav-parent" href="services-850767-875359.html">Services</a>')
    out.append('<div class="nav-drop-panel">')
    out.extend(service_links)
    out.append("</div></div>")
    for href, label, _drop in links[1:]:
        out.append(f'<a href="{href}">{label}</a>')
    out.append("</nav>")
    return "\n".join(out)


def header():
    return f"""<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><div class="topbar-inner"><span>Youngstown, Ohio</span><a href="tel:{PHONE_TEL}">Call {PHONE_DISP}</a></div></div>
<header class="header">
  <div class="header-inner">
    <a class="logo" href="index.html" aria-label="Youngstown Concrete Contractors home"><img class="logo-img" src="images/logo.png" alt="Youngstown Concrete Contractors" width="154" height="64"></a>
    {nav("")}
    <div class="header-cta">
      <a class="btn btn-line" href="tel:{PHONE_TEL}">{PHONE_DISP}</a>
      <a class="btn btn-red" href="#quote">Free quote</a>
    </div>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Open menu"><span></span><span></span><span></span></button>
  </div>
</header>"""


OFFICE_HOURS_DAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
OFFICE_HOURS_TIME = "7 am – 7 pm"


def office_hours_block():
    rows = "".join(f"<div><span>{day}</span><span>{OFFICE_HOURS_TIME}</span></div>" for day in OFFICE_HOURS_DAYS)
    return f'<div class="hours-list">{rows}</div>'


OFFICE_HOURS = "Monday–Sunday: 7 am – 7 pm"


def footer():
    service_items = "\n".join(f'<li><a href="{s["href"]}">{e(s["name"])}</a></li>' for s in SERVICES)
    return f"""<footer class="footer">
  <div class="wrap footer-grid">
    <div>
      <h2>Company</h2>
      <p>Youngstown Concrete Contractors pours and replaces driveways, patios, and other flatwork, and paves asphalt, for homes and small lots in Youngstown, Ohio.</p>
      <p><a href="tel:{PHONE_TEL}">{PHONE_DISP}</a><br>Service-area work. No public storefront.</p>
    </div>
    <div>
      <h2>Services</h2>
      <ul>{service_items}</ul>
    </div>
    <div>
      <h2>Quick Links</h2>
      <ul>
        <li><a href="index.html">Home</a></li>
        <li><a href="about.html">About</a></li>
        <li><a href="service-areas.html">Service Areas</a></li>
        <li><a href="faq.html">FAQs</a></li>
        <li><a href="contact.html">Contact</a></li>
        <li><a href="sitemap.xml">Sitemap</a></li>
      </ul>
    </div>
    <div>
      <h2>Office Hours</h2>
      {office_hours_block()}
    </div>
  </div>
  <div class="wrap legal">© 2026 Youngstown Concrete Contractors. Estimates come from a look at the property.</div>
</footer>
<nav class="callbar" aria-label="Call or request a quote">
  <a class="btn btn-line" href="tel:{PHONE_TEL}">Call</a>
  <a class="btn btn-red" href="#quote">Free quote</a>
</nav>
<script src="js/site.js"></script>
<script>var d=document,w="https://tally.so/widgets/embed.js",v=function(){{"undefined"!=typeof Tally?Tally.loadEmbeds():d.querySelectorAll("iframe[data-tally-src]:not([src])").forEach((function(el){{el.src=el.dataset.tallySrc}}))}};if("undefined"!=typeof Tally)v();else if(d.querySelector('script[src="'+w+'"]')==null){{var s=d.createElement("script");s.src=w;s.onload=v;s.onerror=v;d.body.appendChild(s);}}</script>
"""


def schema_business():
    areas = [{"@type": "City", "name": f"{loc['name']}, Ohio"} for loc in LOCATIONS]
    areas.insert(0, {"@type": "City", "name": "Youngstown, Ohio"})
    data = {
        "@context": "https://schema.org",
        "@type": "GeneralContractor",
        "name": BRAND,
        "alternateName": "Concrete Youngstown",
        "url": SITE + "/",
        "telephone": "+1-330-293-2914",
        "image": SITE + "/images/driveways-1.jpg",
        "logo": SITE + "/images/logo.png",
        "description": "Concrete driveways, patios, stamped and stained flatwork, and asphalt paving for homes and small lots in Youngstown, Ohio and nearby communities.",
        "areaServed": areas,
        "knowsAbout": [s["name"] for s in SERVICES],
    }
    import json
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + "</script>"


def schema_faq(items):
    import json
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in items
        ],
    }
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + "</script>"


def crumbs_schema(items):
    import json
    data = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": name, "item": SITE + "/" + href if href else SITE + "/"}
            for i, (name, href) in enumerate(items)
        ],
    }
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + "</script>"


def page(filename, title, desc, body, canonical, image, extra_head="", robots="index, follow"):
    url = canonical
    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{e(url)}">
<meta name="theme-color" content="#111111">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<meta property="og:site_name" content="Youngstown Concrete Contractors">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{e(url)}">
<meta property="og:type" content="website">
<meta property="og:image" content="{e(image)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@500;600&amp;family=Source+Sans+3:wght@400;600;700&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/styles.css">
{extra_head}
</head>
<body>
{header()}
<main id="main">
{body}
</main>
{footer()}
</body>
</html>
"""
    (ROOT / filename).write_text(doc, encoding="utf-8")


def li(items):
    return "<ul>" + "".join(f"<li>{e(x)}</li>" for x in items) + "</ul>"


def home():
    cards = []
    for s in SERVICES:
        cards.append(f"""<a class="card" href="{s["href"]}">
        <img src="{s["img"]}" alt="{e(s["alt"])}">
        <span class="card-body"><h3>{e(s["name"])}</h3><p>{e(s["card"])}</p><span class="more">Details</span></span>
      </a>""")
    towns = "".join(f'<a href="{loc["href"]}">{e(loc["name"])}</a>' for loc in LOCATIONS)
    gallery_items = [
        ("images/driveways-2.jpg", "Screeding fresh concrete with a long straightedge"),
        ("images/stained-2.jpg", "Troweling a concrete floor surface along a wall"),
        ("images/stamped-1.jpg", "Finishing a concrete slab with a steel trowel"),
        ("images/asphalt-1.jpg", "Hand-floating wet concrete inside forms"),
        ("images/installation-2.jpg", "Placing concrete over steel reinforcement on a slab"),
        ("images/patios-2.jpg", "Concrete discharging from a hopper onto a reinforced slab"),
    ]
    gallery = "".join(
        f'<figure class="service-shot"><img src="{src}" alt="{e(alt)}" loading="lazy" decoding="async"></figure>'
        for src, alt in gallery_items
    )
    body = f"""
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <p class="kicker">Youngstown, Ohio</p>
      <h1>Concrete Contractors Youngstown Ohio</h1>
      <p class="lede">Youngstown Ohio Concrete Contractors provides professional residential and commercial concrete services throughout Youngstown, Ohio, and surrounding communities. We specialize in <a class="inline" href="concrete-driveways.html">concrete driveway installation and replacement</a>, <a class="inline" href="concrete-patios.html">concrete patios</a>, <a class="inline" href="stamped-concrete.html">stamped concrete</a>, <a class="inline" href="stained-concrete.html">stained concrete</a>, and <a class="inline" href="asphalt-paving.html">asphalt paving</a> for homes, businesses, and small parking lots. Whether you're looking to replace a cracked driveway, install a beautiful backyard patio, upgrade your outdoor space with decorative concrete, or improve your property's curb appeal, our team delivers quality workmanship and durable, long-lasting results. We focus on proper site preparation, reliable materials, attention to detail, and customer satisfaction on every project. Unlike contractors who provide estimates based solely on photographs, we evaluate your property in person to provide accurate quotes tailored to your specific needs. From small residential improvements to larger commercial concrete projects, Youngstown Ohio Concrete Contractors is committed to dependable service, competitive pricing, and professional results.</p>
      <div class="hero-actions">
        <a class="btn btn-ghost" href="tel:{PHONE_TEL}">Call {PHONE_DISP}</a>
      </div>
    </div>
    {tally_block()}
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="section-head">
      <p class="kicker">Services</p>
      <h2>What we pour and pave</h2>
      <p>Start with the surface you need. A salt-scaled driveway, a backyard patio, and a shed pad are not the same job, even though all of them are concrete.</p>
    </div>
    <div class="cards">{"".join(cards)}</div>
    <p style="margin-top:1.25rem"><a href="services-850767-875359.html">See all services</a></p>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="section-head">
      <p class="kicker">Why choose us</p>
      <h2>Why Choose Youngstown Concrete Contractors</h2>
    </div>
    <div class="factors">
      <article class="factor"><span>Priced from the property</span><p>We measure the slab, the grade, and the truck access before we write a number. A photo starts the conversation. It does not set the price.</p></article>
      <article class="factor"><span>Repair or replace, said plainly</span><p>If a panel can stay, we say so. If the slab has failed, we say replacement and explain why, instead of covering it.</p></article>
      <article class="factor"><span>Built for Youngstown winters</span><p>Base, slope, joints, and drainage are planned for freeze-thaw, road salt, and the clay soils common through the Mahoning Valley.</p></article>
      <article class="factor"><span>Finish matched to the slab</span><p>Broom finish for most drives. Stamped and stained work where the concrete is new or still sound, not as a cover for damage.</p></article>
    </div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap split">
    <article class="panel">
      <img src="images/patios-2.jpg" alt="Concrete discharging from a hopper onto a reinforced slab">
      <h2>Houses</h2>
      <p>Most calls are a driveway that has scaled, a patio that pitches toward the house, or a walk that has become a trip edge. We replace the failed concrete, set the slope, and finish it for winter in Mahoning County.</p>
      <p><a href="concrete-driveways.html">Driveway replacement</a> · <a href="concrete-patios.html">Patios</a></p>
    </article>
    <article class="panel">
      <img src="images/services.jpg" alt="Crew placing concrete from a chute on a job site">
      <h2>Small lots</h2>
      <p>Shops and houses sometimes need a parking pad, an apron, or a short run of asphalt rather than a backyard patio. The scope is still flatwork. We are not paving highways or pouring building foundations.</p>
      <p><a href="asphalt-paving.html">Asphalt paving</a> · <a href="concrete-installation.html">Pads and sidewalks</a></p>
    </article>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="section-head">
      <p class="kicker">Gallery</p>
      <h2>Flatwork in progress</h2>
      <p>Finishing, floating, and placing concrete. Call {PHONE_DISP} to talk about your own slab.</p>
    </div>
    <div class="home-gallery">{gallery}</div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="section-head">
      <p class="kicker">Our process</p>
      <h2>How a concrete job gets priced</h2>
    </div>
    <div class="steps">
      <article class="step"><span>01</span><h3>Name the slab</h3><p>Driveway, patio, walk, pad, or asphalt. If the old surface has failed, say so. Repair and replacement are different estimates.</p></article>
      <article class="step"><span>02</span><h3>Look at water and access</h3><p>Clay soils in the valley hold water. A truck that cannot reach the forms changes the labor. Both show up when we stand on the lot.</p></article>
      <article class="step"><span>03</span><h3>Choose a finish that fits</h3><p>Broom finish for most drives. Stamp or stain when the slab is new or still sound and you want color or pattern. We will say if the finish you like is the wrong one for winter.</p></article>
    </div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="section-head">
      <p class="kicker">Service area</p>
      <h2>Youngstown and nearby towns</h2>
      <p>Youngstown Concrete Contractors works in Youngstown and the communities around it. <a href="service-areas.html">All service areas</a>.</p>
    </div>
    <div class="towns">{towns}</div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="section-head">
      <p class="kicker">Reviews</p>
      <h2>Talk to us before you decide</h2>
      <p>We would rather you hear how we work than read a quote about it. Call <a href="tel:{PHONE_TEL}">{PHONE_DISP}</a> and describe the slab, or send the form above.</p>
    </div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="section-head">
      <p class="kicker">Questions</p>
      <h2>Before you request a number</h2>
      <p><a href="faq.html">More concrete questions</a></p>
    </div>
    {faq_html(HOME_FAQS)}
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="cta-band">
      <div>
        <h2>Ready to talk through the slab?</h2>
        <p>Call {PHONE_DISP} or send the details. We price the job from the property.</p>
      </div>
      <div class="hero-actions">
        <a class="btn btn-red" href="tel:{PHONE_TEL}">Call {PHONE_DISP}</a>
        <a class="btn btn-ghost" href="#quote">Request an estimate</a>
      </div>
    </div>
  </div>
</section>
"""
    page(
        "index.html",
        "Concrete Contractors Youngstown Ohio | Concrete Driveways, Patios, Walkways",
        "Youngstown Ohio Concrete Contractors provides residential and commercial concrete services in Youngstown, OH: driveways, patios, stamped and stained concrete, and asphalt paving. Call (330) 293-2914.",
        body,
        SITE + "/",
        SITE + "/images/driveways-2.jpg",
        schema_business() + schema_faq(HOME_FAQS),
    )


def rich(text):
    """Escape text but keep simple internal <a href="...">...</a> links."""
    parts = []
    pos = 0
    for m in re.finditer(r'<a href="([a-z0-9./#-]+)">([^<]+)</a>', text):
        parts.append(e(text[pos:m.start()]))
        parts.append(f'<a href="{e(m.group(1))}">{e(m.group(2))}</a>')
        pos = m.end()
    parts.append(e(text[pos:]))
    return "".join(parts)


def render_service_sections(sections):
    out = []
    for sec in sections:
        out.append(f'<h2>{e(sec["h2"])}</h2>')
        if sec.get("lead"):
            out.append(f'<p>{rich(sec["lead"])}</p>')
        for p in sec.get("paragraphs") or []:
            out.append(f"<p>{rich(p)}</p>")
        if sec.get("bullets"):
            out.append("<ul>" + "".join(f"<li>{rich(x)}</li>" for x in sec["bullets"]) + "</ul>")
        for title, body in sec.get("subs") or []:
            out.append(f"<h3>{e(title)}</h3>")
            out.append(f"<p>{rich(body)}</p>")
        if sec.get("steps"):
            steps = "".join(
                f'<article class="step"><span>{e(n)}</span><h3>{e(title)}</h3><p>{rich(body)}</p></article>'
                for n, title, body in sec["steps"]
            )
            out.append(f'<div class="steps">{steps}</div>')
    return "\n".join(out)


def service_page(s):
    others = [o for o in SERVICES if o["href"] != s["href"]]
    related = "".join(f'<li><a href="{o["href"]}">{e(o["name"])}</a></li>' for o in others)
    second = others[SERVICES.index(s) % len(others)]
    gallery = (
        f'<div class="service-gallery">'
        f'<figure class="service-shot"><img src="{s["img"]}" alt="{e(s["alt"])}" loading="lazy" decoding="async"></figure>'
        f'<figure class="service-shot"><img src="{second["img"]}" alt="{e(second["alt"])}" loading="lazy" decoding="async"></figure>'
        f"</div>"
    )
    towns = "".join(f'<a href="{loc["href"]}">{e(loc["name"])}</a>' for loc in LOCATIONS)
    intro = s["intro"] if isinstance(s["intro"], (list, tuple)) else [s["intro"]]
    hero = page_hero(
        "",
        e(s["h1"]),
        [e(x) for x in intro],
        s["hero"],
        actions=f'<a class="btn btn-red" href="tel:{PHONE_TEL}">Call {PHONE_DISP} for a Free Estimate</a>',
        eyebrow=s["name"],
        extra_class="service-hero",
    )
    next_href, next_label = s["next"]
    cta_title = s.get("cta_title") or ("Request a Free " + s["name"] + " Estimate")
    cta_text = s.get("cta_text") or (
        "Contact Youngstown Concrete Contractors to discuss your project."
    )
    body = f"""
<div class="crumb-bar"><div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> · <a href="services-850767-875359.html">Services</a> · <span aria-current="page">{e(s["name"])}</span></nav></div></div>
{hero}
<section class="section service-body">
  <div class="wrap service-layout">
    <div class="service-main">
      {gallery}
      <div class="prose service-copy">
        {render_service_sections(s["sections"])}
        <h2>Frequently Asked Questions</h2>
        {faq_html(s["faqs"])}
      </div>
    </div>
    <aside class="service-aside" aria-label="Estimate and related services">
      <div class="side-card">
        <p class="side-kicker">Talk through the pour</p>
        <p>Call or send the address and what the slab is for. We will tell you if it is a repair, a replacement, or a different finish than you started with.</p>
        <p class="side-phone"><a href="tel:{PHONE_TEL}">{PHONE_DISP}</a></p>
        <p class="side-hours">{OFFICE_HOURS}</p>
        <p><a class="btn btn-red" href="#quote">Request an estimate</a></p>
      </div>
      <div class="side-card side-card-muted">
        <p class="side-kicker">Related</p>
        <ul class="side-links">{related}</ul>
      </div>
    </aside>
  </div>
</section>
<section class="section section-towns" style="padding-top:0">
  <div class="wrap">
    <h2>Towns we serve</h2>
    <div class="towns">{towns}</div>
    <p style="margin-top:1rem"><a href="service-areas.html">Service areas</a> · <a href="{next_href}">{e(next_label)}</a> · <a href="services-850767-875359.html">All services</a></p>
  </div>
</section>
{cta_band(cta_title, cta_text)}
"""
    page(
        s["href"],
        s["title"],
        s["desc"],
        body,
        SITE + "/" + s["href"],
        SITE + "/" + s["img"],
        schema_faq(s["faqs"])
        + crumbs_schema(
            [
                ("Home", ""),
                ("Services", "services-850767-875359.html"),
                (s["name"], s["href"]),
            ]
        ),
    )


def services_index():
    cards = []
    for s in SERVICES:
        cards.append(f"""<a class="card" href="{s["href"]}">
        <img src="{s["img"]}" alt="{e(s["alt"])}">
        <span class="card-body"><h3>{e(s["name"])}</h3><p>{e(s["card"])}</p><span class="more">Details</span></span>
      </a>""")
    body = f"""
{page_hero('<p class="crumbs"><a href="index.html">Home</a> · Services</p>', "Concrete Services in Youngstown, Ohio", ["Six kinds of flatwork, each with its own page. Pick the one that matches the slab you have, or call " + PHONE_DISP + " and describe the failure. We will point you to the right scope."], "images/services.jpg")}
<section class="section"><div class="wrap"><div class="cards">{"".join(cards)}</div></div></section>
"""
    page(
        "services-850767-875359.html",
        "Concrete Services | Youngstown Concrete Contractors",
        "Driveways, patios, stamped concrete, stained concrete, flatwork, and asphalt paving in Youngstown, Ohio. Call (330) 293-2914.",
        body,
        SITE + "/services-850767-875359.html",
        SITE + "/images/services.jpg",
        crumbs_schema([("Home", ""), ("Services", "services-850767-875359.html")]),
    )


def location_page(loc):
    jobs = "".join(
        f'<article class="factor"><span><a href="{href}">{e(title)}</a></span><p>{e(text)}</p></article>'
        for href, title, text in loc["jobs"]
    )
    others = "".join(f'<a href="{o["href"]}">{e(o["name"])}</a>' for o in LOCATIONS if o["href"] != loc["href"])
    body = f"""
{page_hero('<p class="crumbs"><a href="index.html">Home</a> · <a href="service-areas.html">Service areas</a> · ' + e(loc["name"]) + '</p>', e(loc["h1"]), [e(loc["intro"])], "images/driveways-1.jpg")}
<section class="section">
  <div class="wrap">
    <div class="media-row">
      <img src="images/installation-2.jpg" alt="Placing concrete over steel reinforcement on a slab">
      <div>
        <h2>What changes on a {e(loc["name"])} lot</h2>
        <p>{e(loc["detail"])}</p>
      </div>
    </div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="section-head"><p class="kicker">Work</p><h2>Jobs we take in {e(loc["name"])}</h2></div>
    <div class="factors">{jobs}</div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="section-head"><p class="kicker">Questions</p><h2>{e(loc["name"])} concrete questions</h2></div>
    {faq_html(loc["faqs"])}
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    <h2>Other towns</h2>
    <div class="related">{others}</div>
    <p style="margin-top:1rem"><a href="service-areas.html">Back to all service areas</a></p>
  </div>
</section>
"""
    page(
        loc["href"],
        loc["title"],
        loc["desc"],
        body,
        SITE + "/" + loc["href"],
        SITE + "/images/driveways-1.jpg",
        schema_faq(loc["faqs"]) + crumbs_schema([("Home", ""), ("Service areas", "service-areas.html"), (loc["name"], loc["href"])]),
    )


def service_areas():
    blocks = []
    for loc in LOCATIONS:
        parts = loc["intro"].split(". ")
        text = parts[0] + "."
        if len(text) < 110 and len(parts) > 1:
            text = parts[0] + ". " + parts[1]
            if not text.endswith("."):
                text += "."
        blocks.append(f'<article class="factor"><span><a href="{loc["href"]}">{e(loc["name"])}, Ohio</a></span><p>{e(text)}</p></article>')
    body = f"""
{page_hero('<p class="crumbs"><a href="index.html">Home</a> · Service areas</p>', "Concrete Service Areas around Youngstown", ["Youngstown Concrete Contractors works in Youngstown and the towns around it in Mahoning County and nearby Trumbull County. Each page below is about the flatwork on those lots: access, drainage, salt, and the kind of slab we are usually replacing. It is not a town history."], "images/driveways-2.jpg")}
<section class="section"><div class="wrap"><div class="factors">{"".join(blocks)}</div></div></section>
<section class="section" style="padding-top:0">
  <div class="wrap prose">
    <h2>Youngstown itself</h2>
    <p>In the city, drives are often shorter, trucks have less room, and the concrete has already lived through a lot of salt. The service pages for <a href="concrete-driveways.html">driveways</a>, <a href="concrete-patios.html">patios</a>, <a href="stamped-concrete.html">stamped concrete</a>, <a href="stained-concrete.html">stained concrete</a>, <a href="asphalt-paving.html">asphalt</a>, and <a href="concrete-installation.html">other flatwork</a> are written for that work. If your street is in Youngstown, start there or send the form.</p>
  </div>
</section>
"""
    page(
        "service-areas.html",
        "Service Areas | Youngstown Concrete Contractors",
        "Concrete and asphalt flatwork in Youngstown, Boardman, Austintown, Canfield, Poland, Struthers, Warren, Niles, Girard, Hubbard, and Campbell.",
        body,
        SITE + "/service-areas.html",
        SITE + "/images/driveways-2.jpg",
        crumbs_schema([("Home", ""), ("Service areas", "service-areas.html")]),
    )


def about():
    body = f"""
{page_hero('<p class="crumbs"><a href="index.html">Home</a> · About</p>', "About Youngstown Concrete Contractors", ["Youngstown Concrete Contractors is a service-area concrete crew for Youngstown and the towns around it. Driveways, patios, stamped and stained flatwork, sidewalks, small pads, and asphalt paving. There is no showroom and no public storefront. The estimate starts with the slab you have."], "images/services.jpg")}
<section class="section">
  <div class="wrap split">
    <div class="prose">
      <h2>What we do on a job</h2>
      <p>We look at the concrete, the grade, and the access. If the slab has failed, we say replacement. If a panel can stay, we say that too. Decorative work is offered when the concrete is new or still sound, not as a cover for damage.</p>
      <p>Winters here are part of the plan. Freeze-thaw, road salt, and clay soils that hold water show up on driveways from Youngstown to Warren. Joints, base, and slope matter more than a slogan on a truck.</p>
      <p>We do not publish a street address, a license number, a warranty term, or a year founded, because those are not things to invent for a webpage. If you need a document for a permit or a property manager, ask when we write the estimate and we will tell you what we can provide.</p>
      <p><a href="service-areas.html">See the service area</a> or go through the <a href="services-850767-875359.html">services</a>.</p>
    </div>
    <div>
      <img src="images/installation-1.jpg" alt="Finishing the edge of a new concrete sidewalk" style="border-radius:16px;width:100%;height:320px;object-fit:cover">
    </div>
  </div>
</section>
"""
    page(
        "about.html",
        "About Youngstown Concrete Contractors | Youngstown, OH",
        "Youngstown Concrete Contractors is a service-area crew for driveways, patios, decorative flatwork, and asphalt in Youngstown, Ohio. Call (330) 293-2914.",
        body,
        SITE + "/about.html",
        SITE + "/images/services.jpg",
        crumbs_schema([("Home", ""), ("About", "about.html")]),
    )


def contact():
    body = f"""
{page_hero('<p class="crumbs"><a href="index.html">Home</a> · Contact</p>', "Request a Concrete Estimate", ['Call <a class="inline" href="tel:' + PHONE_TEL + '">' + PHONE_DISP + '</a> or use the form. Include the city, whether this is a new pour or a replacement, and roughly what the slab is for. We schedule a look before we price it.'], "images/installation-1.jpg")}
<section class="section">
  <div class="wrap split">
    <div class="prose">
      <h2>Reach Youngstown Concrete Contractors</h2>
      <p>Phone: <a href="tel:{PHONE_TEL}">{PHONE_DISP}</a></p>
      <p>Service-area work. No public storefront. We serve Youngstown and nearby towns listed on the <a href="service-areas.html">service areas</a> page.</p>
      <p>Not sure which service fits? Start with the <a href="services-850767-875359.html">services</a> overview.</p>
    </div>
    <div>
      <h2>Office hours</h2>
      {office_hours_block()}
    </div>
  </div>
</section>
"""
    page(
        "contact.html",
        "Contact Youngstown Concrete Contractors | Free Estimate",
        "Call (330) 293-2914 or request a concrete estimate in Youngstown, Ohio. Driveways, patios, stamped concrete, stain, and asphalt.",
        body,
        SITE + "/contact.html",
        SITE + "/images/installation-1.jpg",
        crumbs_schema([("Home", ""), ("Contact", "contact.html")]),
    )


def faq_page():
    all_items = HOME_FAQS + MORE_FAQS
    body = f"""
{page_hero('<p class="crumbs"><a href="index.html">Home</a> · FAQs</p>', "Concrete Questions in Youngstown", ["Straight answers about cost, replacement, decorative finishes, and where we work. Service pages have more specific questions for that slab."], "images/patios-1.jpg")}
<section class="section"><div class="wrap">{faq_html(all_items)}
  <p>Looking for a single service? Read the <a href="concrete-driveways.html">driveway</a>, <a href="concrete-patios.html">patio</a>, <a href="stamped-concrete.html">stamped</a>, <a href="stained-concrete.html">stained</a>, <a href="asphalt-paving.html">asphalt</a>, or <a href="concrete-installation.html">installation</a> page.</p>
</div></section>
"""
    page(
        "faq.html",
        "Concrete FAQs | Youngstown Concrete Contractors",
        "Answers about concrete driveway cost, replacement, stamped and stained finishes, and service towns around Youngstown. Call (330) 293-2914.",
        body,
        SITE + "/faq.html",
        SITE + "/images/patios-1.jpg",
        schema_faq(all_items) + crumbs_schema([("Home", ""), ("FAQs", "faq.html")]),
    )


def sitemap():
    urls = ["", "about.html", "contact.html", "faq.html", "service-areas.html", "services-850767-875359.html"]
    urls += [s["href"] for s in SERVICES]
    urls += [loc["href"] for loc in LOCATIONS]
    # unique, home canonical is /
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    seen = set()
    for u in urls:
        loc = SITE + "/" + u
        if loc in seen:
            continue
        seen.add(loc)
        lines.append(f"  <url><loc>{loc}</loc><lastmod>2026-10-16</lastmod></url>")
    lines.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (ROOT / "robots.txt").write_text(
        "User-agent: *\nAllow: /\nSitemap: https://www.concreteyoungstown.net/sitemap.xml\n",
        encoding="utf-8",
    )


def main():
    counts = [words(s["card"]) for s in SERVICES]
    print("card words", counts)
    if max(counts) - min(counts) > 4:
        raise SystemExit("card descriptions differ too much")
    for s in SERVICES:
        if not (4 <= len(s["faqs"]) <= 6):
            raise SystemExit("faq count " + s["href"])
        for q, a in s["faqs"]:
            n = a.count(".") + a.count("?")
            if n < 2:
                raise SystemExit("short answer " + q)
    home()
    services_index()
    about()
    contact()
    faq_page()
    service_areas()
    for s in SERVICES:
        service_page(s)
    for loc in LOCATIONS:
        location_page(loc)
    sitemap()
    print("wrote pages")


if __name__ == "__main__":
    main()
