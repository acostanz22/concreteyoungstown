# -*- coding: utf-8 -*-
"""Generate the static Concrete Youngstown site."""
import html
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
PHONE_DISP = "(330) 293-2914"
PHONE_TEL = "+13302932914"
SITE = "https://www.concreteyoungstown.net"
SOURCE = "Concrete%20Youngstown"
TALLY = (
    "https://tally.so/embed/xX6B0y?alignLeft=1&hideTitle=1"
    "&transparentBackground=1&dynamicHeight=1&source=" + SOURCE
)

def e(text):
    return html.escape(text, quote=True)

LOGO = """<svg class="logo-mark" viewBox="0 0 42 42" aria-hidden="true">
  <rect x="3" y="6" width="36" height="30" rx="3" fill="none" stroke="#ffffff" stroke-width="2.4"/>
  <path d="M3 21h36" stroke="#d0121a" stroke-width="2.4"/>
  <path d="M21 6v30" stroke="#ffffff" stroke-width="1.6" opacity="0.55"/>
</svg>"""

SERVICES = [
    {
        "href": "stamped-concrete.html",
        "name": "Stamped Concrete",
        "card": "Patterns pressed into fresh concrete for patios, walks, and driveways. Choose the pattern before the pour. Stamping finishes new flatwork. It does not repair a slab that has already cracked or settled.",
        "img": "images/stamped-2.jpg",
        "alt": "Smoothing fresh concrete with a hand float before a decorative finish",
        "title": "Stamped Concrete in Youngstown, Ohio | Concrete Youngstown",
        "desc": "Stamped concrete for Youngstown patios, walks, and driveways. Pattern, color, and texture are set on site before the pour. Call (330) 293-2914.",
        "h1": "Stamped Concrete in Youngstown, Ohio",
        "hero": "images/stamped-2.jpg",
        "intro": "Stamped concrete is a way to put a stone, slate, or brick pattern into a new slab while it is still workable. Homeowners in Youngstown use it for patios, front walks, and sometimes driveways when they want that look without setting individual pavers. The pattern, color, and texture have to be chosen before the truck is scheduled.",
        "when_title": "When stamped concrete is the right job",
        "when": [
            "You want a patio or walk with the look of stone or brick, and the area is being poured new.",
            "A broom-finish slab is structurally fine for the job, but the plain gray surface is not the look you want at the back door or the front walk.",
            "The existing concrete has failed. Stamping does not go on top of a cracked or rocking slab. That is a replacement, then a stamp on the new pour.",
        ],
        "aside_title": "The pattern is part of the pour",
        "aside": "Mats are pressed while the surface is still plastic, then a release agent keeps the mats from sticking. Once the slab has hardened, the pattern is in the concrete. A later stain can shift the color, but it will not add a texture that was never stamped.",
        "process": [
            ("01", "Choose the pattern", "We look at the area, the sun, and how the space is used, then pick a pattern and color that fit. A busy stamp on a small walk can look crowded. A quieter texture often wears better on a driveway."),
            ("02", "Prepare the base", "The old material comes out if it has failed. The grade is set so water leaves the house, and forms are placed for the thickness the use requires."),
            ("03", "Pour and stamp", "Concrete is placed, leveled, and stamped in the window while it can still take a print. Edges, joints, and any steps are finished in the same visit."),
            ("04", "Cure, then wash", "The surface needs time before it is washed and opened to use. We tell you when foot traffic is reasonable. Furniture and vehicles wait longer, especially on cold nights."),
        ],
        "costs": [
            ("Area and shape", "A simple rectangle is a different pour from a patio with a curve, a step, or a seat edge. More edge and more cuts take more time."),
            ("Pattern and color", "Integral color, release, and the stamp mats themselves change the job. A single field pattern costs less to place than a border plus a field."),
            ("Removal and access", "Breaking out an old patio, hauling it, and moving concrete by buggy through a side yard all show up on the estimate."),
            ("Base and drainage", "Soft spots, a slope toward the house, or a patio that has to meet a door threshold can add base work before anyone stamps a pattern."),
            ("Sealer later", "Many stamped surfaces are sealed after they cure. That is a separate step from the pour, and it is maintenance, not a one-time shield against salt or snow shovels."),
        ],
        "faqs": [
            ("Can you stamp a driveway, or only a patio?", "We can stamp a driveway if the slope, the joints, and the texture still make sense for cars and for winter. A deep, irregular stone pattern can be harder to shovel and can hold ice. A lighter texture is often the better driveway choice. We will say so on the walkthrough if the pattern you like belongs on the patio instead."),
            ("Does stamped concrete get slippery when it rains or ices over?", "A textured stamp usually has more grip than a hard-troweled, slick finish. A sealed surface can still be slippery when it is wet or icy, which matters on a walk and near a door. We pick texture with that in mind. No finish is a substitute for clearing snow and ice."),
            ("Can you stamp over the concrete I already have?", "No. The pattern has to be pressed into concrete that is still fresh. If the slab you have is sound and you only want color, look at stained concrete. If it is cracked, scaled, or settled, the honest fix is removal and a new pour."),
            ("How do I choose a pattern without seeing it on my house?", "We narrow it to a few patterns that fit the size of the area and the style of the house, and we look at samples in daylight. A small sample will not match the full patio exactly, because release color and the hand work vary across a larger surface. The goal is a pattern you can live with, not a catalog photo."),
            ("Will a sealer keep road salt from marking the surface?", "A sealer can slow staining and make the color easier to clean. It does not make the slab immune to salt, fertilizer, or a metal shovel. Plan on renewing sealer when it wears, and go easy on deicers the first winter. We will not tell you a sealer is a warranty against Ohio winters."),
            ("How long before we can put the table back?", "Foot traffic comes before furniture. Legs and grill wheels point-load a young slab, so the wait is longer than walking across it. Cold weather stretches that window. We will give you a clear time before we leave, based on the pour and the forecast."),
        ],
        "next": ("concrete-driveways.html", "Concrete driveways"),
    },
    {
        "href": "concrete-driveways.html",
        "name": "Concrete Driveways",
        "card": "New and replacement driveways for homes around Youngstown. The job covers removal, a compacted base, the pour, and a finish sloped off the garage. Thickness follows the vehicles that will use it.",
        "img": "images/driveways-1.jpg",
        "alt": "A worker floating a freshly poured concrete driveway",
        "title": "Concrete Driveways in Youngstown, Ohio | Concrete Youngstown",
        "desc": "Concrete driveway replacement and new pours in Youngstown, Ohio. Removal, base, slope, and finish are set on site. Call (330) 293-2914 for an estimate.",
        "h1": "Concrete Driveways in Youngstown, Ohio",
        "hero": "images/driveways-1.jpg",
        "intro": "A concrete driveway in Youngstown has to live with freeze-thaw, road salt, and the clay soils common through the Mahoning Valley. Most of the calls we get are replacements: the old slab is scaled, cracked into pieces, or pitched back toward the garage. We measure the drive, the garage lip, and the sidewalk before we talk about a price.",
        "when_title": "When a driveway needs to be replaced",
        "when": [
            "The surface is scaling or pitting from salt and freeze-thaw, and the paste is gone down to the stone.",
            "Slabs have settled, rocked, or heaved so water sits against the garage or runs toward the foundation.",
            "Cracks have opened wide enough that a joint filler will not hold, or the drive is too high to meet the sidewalk.",
        ],
        "aside_title": "Slope and the garage floor",
        "aside": "The new drive has to meet the garage without a trip lip and still fall away from the house. On a short Youngstown driveway that can be a tight bit of grade. We set that before forms go in, not after the concrete is down.",
        "process": [
            ("01", "Measure the drive", "We check length, width, garage height, sidewalk elevation, and where water goes now. Photos help us call you back. They are not a substitute for standing on the lot."),
            ("02", "Remove what failed", "Broken concrete is broken out and hauled away when it cannot stay. A sound panel can sometimes remain and be tied to the new work. We do not pour a thin layer over a slab that is still moving."),
            ("03", "Base, forms, pour", "The stone base is compacted, forms are set, and the concrete is placed and finished. Control joints are cut or tooled so the slab has a place to crack in a straight line."),
            ("04", "Cure before you park", "Passenger cars stay off for several days. Cold nights make that longer. We will tell you the wait before we leave. The slab keeps gaining strength after that."),
        ],
        "costs": [
            ("Square footage and thickness", "A passenger-car drive is often about 4 inches over a compacted base. A truck, a boat, or a dumpster pad needs more thickness. We set that from how you use the drive."),
            ("Removal and disposal", "Breaking out a thick old slab, and getting the debris off a tight lot, is a large part of many replacement estimates."),
            ("Access", "If the truck cannot reach the forms, concrete moves by buggy or pump. Narrow side yards in older neighborhoods change the price more than the finish does."),
            ("Reinforcement and joints", "Wire or rebar, and the joint layout, depend on the shape of the drive and the base under it. A long, narrow drive is jointed differently from a wide apron."),
            ("Finish and drainage", "Broom finish is the usual driveway surface. A stamp, a thickened edge, a drain, or rebuilding the swale beside the drive are extras we price only if the lot needs them."),
        ],
        "faqs": [
            ("How thick should a residential driveway be?", "For cars, about 4 inches of concrete over a compacted aggregate base is the usual residential section. Heavier vehicles need a thicker slab, sometimes only in the parking area. We will not quote a thickness from the curb. It depends on the soil, the base, and what you park."),
            ("Can you match the height of my garage floor?", "Yes, that is part of the layout. The drive should meet the slab at the garage without holding water against the door, and it still needs to drain to the street or a yard swale. If the old drive was raised with overlays, we may have to come down to a workable height."),
            ("Do you broom-finish a driveway, or can it be stamped?", "Broom finish is the standard. It sheds water, takes salt and shovels, and is the right surface for most drives. Stamping is available when you want a pattern, with a texture you can still shovel. See the stamped concrete page if that is the look you are after."),
            ("What happens to the old concrete?", "If the slab is failed, we break it out and haul it off. If one panel is sound and at the right height, we can sometimes leave it and dowel the new concrete to it. Leaving a moving slab in place and covering it is how a new surface cracks along the old lines."),
            ("How long before I can drive on it?", "Plan on several days for a passenger car, and longer when the nights are near freezing. Walking on it comes first. We set the actual day from the temperature and the mix before we leave, rather than promising a clock time in advance."),
            ("Will road salt ruin a new driveway?", "Salt and freeze-thaw are hard on any exterior concrete in Youngstown. Air-entrained concrete, joints, and a sound base are how a drive gets through winter. They do not make the surface immune. Go light on deicers the first winter, keep fertilizer off the slab, and shovel with a plastic blade when you can."),
        ],
        "next": ("asphalt-paving.html", "Asphalt paving"),
    },
    {
        "href": "asphalt-paving.html",
        "name": "Asphalt Paving",
        "card": "Asphalt drives and small parking areas where a flexible surface fits the lot. Grading, a stable base, and a paved layer that sheds water are the work. The pavement itself is not a drain.",
        "img": "images/asphalt-2.jpg",
        "alt": "Breaking out a failed pavement surface before a new driveway is placed",
        "title": "Asphalt Paving in Youngstown, Ohio | Concrete Youngstown",
        "desc": "Asphalt driveway and small-lot paving in Youngstown, Ohio. Grade, base, and a surface that sheds water. Call (330) 293-2914 to schedule a look.",
        "h1": "Asphalt Paving in Youngstown, Ohio",
        "hero": "images/asphalt-2.jpg",
        "intro": "Asphalt is a flexible pavement. It can be a practical driveway or small parking area when the lot needs a surface that can flex a little and still shed water. Standard asphalt is not a porous drain. If the grade sends water at the garage, a new black surface will send it there too. We fix the slope as part of the paving, not as an afterthought.",
        "when_title": "When asphalt paving fits",
        "when": [
            "An old asphalt drive has alligator cracking, potholes, or edges that have crumbled back to the stone.",
            "A gravel drive ruts every spring and you want a paved surface for two cars, not a structural concrete slab.",
            "A small parking pad beside a shop or a house needs paving, and concrete is not the better fit for how the base moves.",
        ],
        "aside_title": "Water has to leave the surface",
        "aside": "Dense asphalt sheds water. It does not soak it up. The base under it still has to be stable, and the surface still has to slope away from buildings. A pretty overlay on a sunken, wet base will crack in the same pattern as the pavement it covered.",
        "process": [
            ("01", "Look at the failure", "Alligator cracks usually mean the base, not just the top. A few potholes in an otherwise sound drive are a different repair than a full mill and pave. We say which one you are looking at."),
            ("02", "Grade and base", "Soft material comes out. Stone goes down and is compacted. Edges are held so the mat does not ravel at the grass."),
            ("03", "Pave and compact", "Asphalt is placed and rolled while it is hot enough to compact. Thickness follows the use: a car drive is not a dumpster lane."),
            ("04", "Stay off it while it cools", "You can usually walk a new mat sooner than you can park on it. Hot weather keeps it tender longer. We will tell you when to pull the car back in."),
        ],
        "costs": [
            ("Area and thickness", "Square footage and how many inches of asphalt the traffic needs are the core of the price. A thin skin over a failed base is not a bargain."),
            ("Removal", "Milling or tearing out old asphalt, and hauling it, is separate from the new tonnage."),
            ("Base stone", "A gravel drive that was never built as a pavement often needs stone and grading before the first pass of asphalt."),
            ("Edges and access", "Paving against a garage, a fence, or a tight turn from the street takes more hand work than an open rectangle."),
            ("Drainage", "Rebuilding a swale, raising a settled center, or keeping water out of a basement stair is part of the job when the lot requires it."),
        ],
        "faqs": [
            ("Should I choose asphalt or concrete for a Youngstown driveway?", "Concrete is rigid. It wants a stable base and joints, and it handles summer heat without going soft. Asphalt flexes more, which can suit a base that moves a little, and it is usually faster to put back in service. Both fail if water sits under them. If your lot could go either way, we will talk through it on the visit rather than picking from a slogan."),
            ("Can you pave over the old asphalt?", "Only if the old mat is stable, the edges are sound, and adding height will not block the garage door or send water at the house. Alligator cracking and a soft base need to come out. An overlay on that kind of failure copies the cracks into the new surface."),
            ("How soon can we drive on new asphalt?", "Often the same day or the next, once the mat has cooled and set, but a hot afternoon can keep it tender. Turning the steering wheel in place will scuff a fresh drive. We will give you a time before we leave, matched to the weather that day."),
            ("Do you fill potholes, or only repave the whole drive?", "A tight pothole in a sound drive can be patched. A drive that is a map of cracks needs replacement, because the patch will sit in the same failed base. We would rather tell you that on the visit than sell a patch that will open up by spring."),
            ("Does asphalt drain water through the surface?", "Ordinary driveway asphalt does not. It is paved to shed water to the side or the street. If someone told you asphalt is a porous drainage system, that is a different product than a standard residential mat. Your drive still needs slope."),
            ("When would you seal an asphalt drive?", "Sealer is maintenance on a sound mat, usually after the asphalt has cured, not on the day it is paved. It is not a fix for cracks that go through the mat or for a base that has failed. If you need sealing later, ask when we look at the drive and we will tell you whether the surface is a candidate."),
        ],
        "next": ("stained-concrete.html", "Stained concrete"),
    },
    {
        "href": "stained-concrete.html",
        "name": "Stained Concrete",
        "card": "Color on a sound slab when the concrete is still solid. It changes the look of a patio, walk, or floor. Stain will not bridge cracks or level a section that has settled.",
        "img": "images/stained-1.jpg",
        "alt": "Screeding a fresh concrete slab before the surface is finished",
        "title": "Stained Concrete in Youngstown, Ohio | Concrete Youngstown",
        "desc": "Stained concrete for sound patios, walks, and interior slabs in Youngstown. Color does not repair cracks or settlement. Call (330) 293-2914.",
        "h1": "Stained Concrete in Youngstown, Ohio",
        "hero": "images/stained-1.jpg",
        "intro": "Stain is a color treatment for concrete that is still sound. It can warm up a gray patio, a porch slab, or an interior floor. It is not a resurfacing product. If the slab is scaled from salt, cracked into panels, or tipped toward the house, color will follow every flaw. In that case the conversation is about replacement, not stain.",
        "when_title": "When stain is worth doing",
        "when": [
            "The slab is flat, solid, and you want color without breaking it out.",
            "A new patio or walk is being poured and you want color in or on the surface as part of that job.",
            "You are comparing stain to paint. Paint sits on top and peels. Stain, especially a reactive stain, works in the paste and wears differently.",
        ],
        "aside_title": "The slab has to be ready",
        "aside": "Stain needs a clean, open surface. Sealer, glue, oil, and heavy curing compound block it. We look at the slab first. If the concrete is too tight, too dirty, or too far gone, we will say stain is the wrong tool.",
        "process": [
            ("01", "Test the slab", "We check for sealer, moisture issues, cracks, and whether the surface will take stain. A small test spot tells more than a color chart."),
            ("02", "Clean and prep", "The surface is cleaned so the stain can reach the paste. Coatings that would resist the stain come off, or we stop and talk about another finish."),
            ("03", "Apply the color", "Stain goes down and is worked for an even, mottled, or bordered look, depending on what the concrete will actually do. Concrete color is never as uniform as paint from a can."),
            ("04", "Rinse, dry, protect", "Reactive stains are neutralized and rinsed. The slab has to dry before any sealer. We will tell you when you can walk it and when furniture can come back."),
        ],
        "costs": [
            ("Condition of the slab", "A clean broom finish is straightforward. A sealed, painted, or oil-stained slab can take more prep than the coloring itself."),
            ("Interior or exterior", "An outdoor patio deals with sun, salt, and water. An interior floor deals with foot traffic and rugs. The products and the dry time are not the same."),
            ("Color and variation", "One translucent color is a different application from a layered or sawcut pattern. More detail means more time on the surface."),
            ("Repairs first", "Open cracks, spalls, and trip edges have to be addressed before color, or the stain will highlight them. Some of those repairs are a separate scope."),
            ("Sealer", "Exterior sealer is what makes the color easier to live with. It is a maintenance coating. Sun and shovels wear it off, and it will need to be renewed."),
        ],
        "faqs": [
            ("Will stain hide cracks in my patio?", "No. Stain follows the surface. A crack, a patch, and a trowel mark will still be visible, and color often makes them easier to see. If the crack is a joint doing its job, that is fine. If the slab has separated or settled, fix that before you spend money on color."),
            ("Can you stain a driveway that salt has damaged?", "If the paste is scaling and the stone is showing, stain will look blotchy and will not put the surface back. That driveway wants a replacement or, if the damage is truly shallow and the slab is stable, a different conversation. We will not stain a failing drive and call it repaired."),
            ("What is the difference between stain and paint?", "Paint is a film. It can peel when moisture gets behind it, which is common on an exterior slab. Acid and water-based stains color the concrete itself or soak into it. The result is mottled, not a solid paint chip. If you want a flat, uniform paint color, stain will disappoint you, and paint will disappoint you the first time it peels."),
            ("Can you match a stain color from a photo?", "We can get close to a family of colors: warm brown, tan, terra cotta, soft gray. Concrete takes stain differently from one slab to the next, so a photo from another house is a target, not a promise. A test spot on your concrete is the honest sample."),
            ("Do you stain basement floors and garage slabs?", "Yes, if the slab is sound and dry enough for the product. A garage that takes salt off the car is a hard place for a decorative finish. A basement with moisture coming through the slab needs that problem solved first. Tell us which room it is when you call."),
            ("How do I take care of a stained patio?", "Sweep it, keep fertilizer and harsh deicers off it, and expect to renew the sealer when water no longer beads. Do not scrub it with a harsh acid. If the sealer is worn and the color is still even, maintenance is usually a cleaning and a new coat, not a new stain."),
        ],
        "next": ("concrete-patios.html", "Concrete patios"),
    },
    {
        "href": "concrete-patios.html",
        "name": "Concrete Patios",
        "card": "A level slab outside the back door for a table, a grill, and a drier path. Slope, joints, and thickness are set for Mahoning Valley freeze-thaw, not only for a clear summer weekend.",
        "img": "images/patios-1.jpg",
        "alt": "Hand-floating the edge of a new concrete patio slab",
        "title": "Concrete Patios in Youngstown, Ohio | Concrete Youngstown",
        "desc": "Concrete patio installation in Youngstown, Ohio. Slope, joints, and thickness planned for freeze-thaw and backyard drainage. Call (330) 293-2914.",
        "h1": "Concrete Patios in Youngstown, Ohio",
        "hero": "images/patios-1.jpg",
        "intro": "A patio is the flatwork outside the door you actually use. In Youngstown that means a slab that stays put through freeze-thaw, slopes away from the house, and gives you a place for a table that does not rock. We pour broom-finish and stamped patios, and we replace old slabs that have heaved or that hold water against the foundation.",
        "when_title": "When a patio is the right project",
        "when": [
            "The back door opens onto mud, uneven pavers, or a slab that pitches toward the house.",
            "You want a defined place for seating and a grill, with a walk that connects to the driveway or the side gate.",
            "An old patio has cracked into a trip hazard, or frost has lifted a corner every winter.",
        ],
        "aside_title": "Keep water off the wall",
        "aside": "The patio should fall away from the foundation, about enough to move rain without feeling steep under a chair. Downspouts that dump into the same corner will undo a good slope. We look at those before we set forms.",
        "process": [
            ("01", "Lay out the size", "We mark the patio against the door, the steps, and anything you need to keep, such as an egress window or a hose bib. Bigger is not always better if it blocks drainage."),
            ("02", "Excavate and base", "Topsoil comes out. Stone goes in and is compacted. Organic soil left underneath is why a patio settles on one side."),
            ("03", "Form and pour", "Forms set the slope and the thickness. Concrete is placed, struck off, and finished. Joints are laid out so a crack has a straight place to go."),
            ("04", "Cure, then furnish", "Keep pets, grills, and furniture off until we say the surface is ready. A cold week in spring changes the calendar. We would rather you wait than scar the finish."),
        ],
        "costs": [
            ("Size and thickness", "Area drives the concrete yardage. A patio that will hold a hot tub or a heavy kitchen island needs a thicker section than a chair and a grill."),
            ("Steps and edges", "A step down to the yard, a thickened edge, or a turn around a bay window adds forming. A rectangle on flat ground is the simple version."),
            ("Removal", "An old slab, pavers, or a timber border have to come out and leave. Tight gates mean the debris moves by hand."),
            ("Decorative finish", "Broom finish is the baseline. Integral color or a stamp is a different scope. Those choices are on the stamped concrete page if you want pattern, not just a slab."),
            ("Drainage and access", "Regrading a low spot, extending a downspout, or buggy-ing concrete through the house or a side yard changes the labor more than the concrete price."),
        ],
        "faqs": [
            ("How much slope does a patio need?", "Enough to move water away from the house without making the table feel tilted. We set that in the forms. A dead-flat patio holds ice and rain against the wall. A steep one is unpleasant to sit on. The right fall is a site decision, not a single number for every yard."),
            ("Can you pour a patio up to the back door?", "Yes, if the threshold, the siding, and any step can be detailed so water does not run inside. We will not bury siding or block a weep. If the door is low to the yard, the patio may need to stay slightly below the threshold, with the slope still leaving the house."),
            ("Do I have to remove pavers before a concrete patio?", "Yes. Pavers, sand, and the old base come out so the new stone base sits on firm soil. Pouring over pavers is how the slab rocks later. If some edging or a short walk can stay, we will tell you on site."),
            ("Broom finish or stamped for a backyard patio?", "Broom finish is simpler, grips well, and costs less. Stamped concrete is for when the look of the patio matters as much as the floor space. Both are concrete slabs. The base and the slope are the same kind of work. The finish is what changes."),
            ("Can you add a walk from the patio to the driveway?", "Yes. A walk is often poured with the patio so the joint between them is planned. Tell us if you need room for a mower or a trash bin. A walk that is too narrow becomes the thing you step off every week."),
            ("When can we put furniture on a new patio?", "After the slab has cured enough for point loads. That is longer than the wait for walking, and longer still if nights drop near freezing. We will leave you with a day, not a guess. Dragging a metal table across a green slab will mark it."),
        ],
        "next": ("concrete-installation.html", "Concrete installation"),
    },
    {
        "href": "concrete-installation.html",
        "name": "Concrete Installation",
        "card": "Sidewalks, aprons, shed pads, and other flatwork beyond a full driveway or patio. Each pour is formed for the load it will carry, with joints and drainage set before the concrete truck arrives.",
        "img": "images/installation-1.jpg",
        "alt": "Finishing the edge of a newly poured concrete sidewalk",
        "title": "Concrete Installation in Youngstown, Ohio | Concrete Youngstown",
        "desc": "Concrete flatwork in Youngstown, Ohio: sidewalks, aprons, shed pads, and small slabs. Formed and finished for the load. Call (330) 293-2914.",
        "h1": "Concrete Installation in Youngstown, Ohio",
        "hero": "images/installation-1.jpg",
        "intro": "Concrete installation, on this site, means the flatwork that is not already covered by a driveway or a patio: sidewalks, garage aprons, shed and equipment pads, small approaches, and replacement panels. We form it, place it, and finish it for the load and the weather in the Mahoning Valley. We are not a structural builder of buildings or bridges.",
        "when_title": "When you need a separate pour",
        "when": [
            "A sidewalk panel has heaved into a trip edge, or a city-side walk is yours to replace up to the property line.",
            "You need a pad for a shed, a condenser, a dumpster, or a small parking spot off the main drive.",
            "The apron in front of the garage has broken away from the driveway, and the rest of the drive can stay.",
        ],
        "aside_title": "Match the pour to the load",
        "aside": "A 4-inch sidewalk and a pad that will hold a loaded trailer are not the same slab. Thickness, base, and reinforcement follow the use. We ask what will sit on it before we order concrete.",
        "process": [
            ("01", "Define the pad or walk", "We measure, check the property side of any public walk, and note doors, gates, and utilities. A small pad still needs a plan for water."),
            ("02", "Cut out and base", "Failed concrete is sawed or broken at a joint when only a panel is going. The base is compacted so the new section does not become the low spot."),
            ("03", "Form, place, finish", "Forms hold the line and the slope. Concrete is placed and finished to match the adjacent slab as closely as a new pour can. A patch will not be invisible."),
            ("04", "Joint and cure", "Joints line up with the old work where they should. The new concrete stays protected from pets, salt, and loads until it can take them."),
        ],
        "costs": [
            ("Quantity", "A single sidewalk panel is a different mobilization than a long walk plus a pad. Small pours still need a crew and a truck."),
            ("Thickness and steel", "Light foot traffic and a heavy pad are priced on different sections. We will not use a sidewalk thickness under a trailer."),
            ("Sawcutting and tie-in", "Cutting a clean edge and doweling into sound concrete takes time, and it is what keeps the new panel from rocking against the old one."),
            ("Access and haul-off", "Buckets, buggies, and a long carry from the street add labor. So does bagging debris out of a fenced yard."),
            ("Finish", "Broom finish is standard for walks and pads. A decorative finish belongs on the stamped or stained pages and is priced as that work."),
        ],
        "faqs": [
            ("Can you replace one broken sidewalk square?", "Often, yes, if the squares next to it are stable and we can cut a clean joint. If the whole walk has heaved, replacing one square leaves you with the same trip edge a few feet away. We will tell you how far the failure actually goes."),
            ("Do you pour shed pads and equipment pads?", "Yes. Tell us the shed size or the weight of what will sit there, and whether you need the pad larger than the building for a mower or a door swing. A thin, unreinforced cap on soft ground will crack under a shed that holds tools and a mower."),
            ("Can you do the apron without replacing the whole driveway?", "Yes, when the driveway beyond the apron is sound and at a workable height. The apron takes the impact of the street and the gutter. We tie the new apron into the drive and keep the slope so water is not trapped at the garage."),
            ("Will a new panel match the old concrete color?", "New concrete is lighter and will darken somewhat as it cures, but it rarely disappears into 20-year-old concrete. We can get the finish and the joint close. We will not promise an invisible patch."),
            ("Do you install public sidewalks for the city?", "We pour private walks, aprons, and the portion of a sidewalk that is the owner's to replace. The public walk in the right-of-way is often a city repair. We will point out where our work should stop so you are not paying to rebuild the city's concrete."),
            ("How do you handle a small pour the truck cannot reach?", "We buggy or wheel it from the street if the distance is reasonable. If the carry is long or the gate is too narrow, that labor is on the estimate. Some very small pads are placed from a mixer on site. We decide that after we see the access."),
        ],
        "next": ("stamped-concrete.html", "Stamped concrete"),
    },
]

LOCATIONS = [
    {
        "href": "boardman.html",
        "name": "Boardman",
        "title": "Concrete Contractors in Boardman, Ohio | Concrete Youngstown",
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
        "title": "Concrete Contractors in Austintown, Ohio | Concrete Youngstown",
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
        "title": "Concrete Contractors in Canfield, Ohio | Concrete Youngstown",
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
        "title": "Concrete Contractors in Poland, Ohio | Concrete Youngstown",
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
        "title": "Concrete Contractors in Struthers, Ohio | Concrete Youngstown",
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
        "title": "Concrete Contractors in Warren, Ohio | Concrete Youngstown",
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
        "title": "Concrete Contractors in Niles, Ohio | Concrete Youngstown",
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
        "title": "Concrete Contractors in Girard, Ohio | Concrete Youngstown",
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
        "title": "Concrete Contractors in Hubbard, Ohio | Concrete Youngstown",
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
        "title": "Concrete Contractors in Campbell, Ohio | Concrete Youngstown",
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
      <p class="form-note">Tell us the town, what you want poured or replaced, and a phone number. The form includes a source field so we know the lead came from Concrete Youngstown. Do not send payment information.</p>
      <iframe data-tally-src="{TALLY}" loading="lazy" width="100%" height="552" frameborder="0" marginheight="0" marginwidth="0" title="Get a free quote"></iframe>
    </div>"""


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
    <a class="logo" href="index.html" aria-label="Concrete Youngstown home">{LOGO}<span class="logo-text"><span class="logo-kicker">Concrete</span><span class="logo-name">Youngstown</span></span></a>
    {nav("")}
    <div class="header-cta">
      <a class="btn btn-line" href="tel:{PHONE_TEL}">{PHONE_DISP}</a>
      <a class="btn btn-red" href="#quote">Free quote</a>
    </div>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Open menu"><span></span><span></span><span></span></button>
  </div>
</header>"""


def footer():
    service_items = "\n".join(f'<li><a href="{s["href"]}">{e(s["name"])}</a></li>' for s in SERVICES)
    return f"""<footer class="footer">
  <div class="wrap footer-grid">
    <div>
      <h2>Company</h2>
      <p>Concrete Youngstown pours and replaces driveways, patios, and other flatwork, and paves asphalt, for homes and small lots in Youngstown, Ohio.</p>
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
  </div>
  <div class="wrap legal">© 2026 Concrete Youngstown. Estimates come from a look at the property.</div>
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
        "name": "Concrete Youngstown",
        "alternateName": "Youngstown Ohio Concrete Contractors",
        "url": SITE + "/",
        "telephone": "+1-330-293-2914",
        "image": SITE + "/images/driveways-1.jpg",
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
<meta property="og:site_name" content="Concrete Youngstown">
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
    body = f"""
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <p class="kicker">Youngstown, Ohio</p>
      <h1>Concrete Contractors in Youngstown, Ohio</h1>
      <p class="lede"><a class="inline" href="concrete-driveways.html">Driveways</a>, <a class="inline" href="concrete-patios.html">patios</a>, <a class="inline" href="stamped-concrete.html">stamped</a> and <a class="inline" href="stained-concrete.html">stained</a> flatwork, and <a class="inline" href="asphalt-paving.html">asphalt paving</a> for houses and small lots. Quoted from the property, not from a photo.</p>
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
      <p class="kicker">Before you call</p>
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
      <p>We work in Youngstown and the communities around it. The footer links to this list instead of repeating every town. <a href="service-areas.html">All service areas</a>.</p>
    </div>
    <div class="towns">{towns}</div>
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
        "Concrete Contractors in Youngstown, Ohio | Concrete Youngstown",
        "Concrete driveways, patios, stamped and stained flatwork, and asphalt paving in Youngstown, Ohio. Call (330) 293-2914 for an on-site estimate.",
        body,
        SITE + "/",
        SITE + "/images/driveways-2.jpg",
        schema_business() + schema_faq(HOME_FAQS),
    )


def service_page(s):
    steps = "".join(
        f'<article class="step"><span>{n}</span><h3>{e(title)}</h3><p>{e(text)}</p></article>'
        for n, title, text in s["process"]
    )
    factors = "".join(
        f'<article class="factor"><span>{e(title)}</span><p>{e(text)}</p></article>'
        for title, text in s["costs"]
    )
    related = "".join(
        f'<a href="{o["href"]}">{e(o["name"])}</a>' for o in SERVICES if o["href"] != s["href"]
    )
    body = f"""
<section class="page-hero" style="--hero: url('{s["hero"]}')">
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Home</a> · <a href="services-850767-875359.html">Services</a> · {e(s["name"])}</p>
    <h1>{e(s["h1"])}</h1>
    <p>{e(s["intro"])}</p>
    <div class="hero-actions">
      <a class="btn btn-red" href="tel:{PHONE_TEL}">Call {PHONE_DISP}</a>
      <a class="btn btn-ghost" href="#quote">Request an estimate</a>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="section-head">
      <p class="kicker">When it is needed</p>
      <h2>{e(s["when_title"])}</h2>
    </div>
    {li(s["when"])}
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="media-row">
      <img src="{s["img"]}" alt="{e(s["alt"])}">
      <div>
        <h2>{e(s["aside_title"])}</h2>
        <p>{e(s["aside"])}</p>
      </div>
    </div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="section-head">
      <p class="kicker">Process</p>
      <h2>How the work goes</h2>
    </div>
    <div class="steps">{steps}</div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="section-head">
      <p class="kicker">Cost factors</p>
      <h2>What changes the estimate</h2>
      <p>We do not publish a price per square foot. These are the items that move a quote once we see the lot.</p>
    </div>
    <div class="factors">{factors}</div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="section-head">
      <p class="kicker">Questions</p>
      <h2>Before you schedule</h2>
    </div>
    {faq_html(s["faqs"])}
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    <h2>Related services</h2>
    <p>If this is a different slab than the one you need, start with <a href="{s["next"][0]}">{e(s["next"][1])}</a>.</p>
    <div class="related">{related}</div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    {tally_block()}
    <div class="hero-actions" style="margin-top:1rem">
      <a class="btn btn-dark" href="tel:{PHONE_TEL}">Call {PHONE_DISP}</a>
    </div>
  </div>
</section>
"""
    page(
        s["href"],
        s["title"],
        s["desc"],
        body,
        SITE + "/" + s["href"],
        SITE + "/" + s["img"],
        schema_faq(s["faqs"]) + crumbs_schema([("Home", ""), ("Services", "services-850767-875359.html"), (s["name"], s["href"])]),
    )


def services_index():
    cards = []
    for s in SERVICES:
        cards.append(f"""<a class="card" href="{s["href"]}">
        <img src="{s["img"]}" alt="{e(s["alt"])}">
        <span class="card-body"><h3>{e(s["name"])}</h3><p>{e(s["card"])}</p><span class="more">Details</span></span>
      </a>""")
    body = f"""
<section class="page-hero" style="--hero: url('images/services.jpg')">
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Home</a> · Services</p>
    <h1>Concrete Services in Youngstown, Ohio</h1>
    <p>Six kinds of flatwork, each with its own page. Pick the one that matches the slab you have, or call {PHONE_DISP} and describe the failure. We will point you to the right scope.</p>
    <div class="hero-actions"><a class="btn btn-red" href="tel:{PHONE_TEL}">Call {PHONE_DISP}</a><a class="btn btn-ghost" href="#quote">Request an estimate</a></div>
  </div>
</section>
<section class="section"><div class="wrap"><div class="cards">{"".join(cards)}</div></div></section>
<section class="section" style="padding-top:0"><div class="wrap">{tally_block()}</div></section>
"""
    page(
        "services-850767-875359.html",
        "Concrete Services in Youngstown, Ohio | Concrete Youngstown",
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
<section class="page-hero" style="--hero: url('images/driveways-1.jpg')">
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Home</a> · <a href="service-areas.html">Service areas</a> · {e(loc["name"])}</p>
    <h1>{e(loc["h1"])}</h1>
    <p>{e(loc["intro"])}</p>
    <div class="hero-actions"><a class="btn btn-red" href="tel:{PHONE_TEL}">Call {PHONE_DISP}</a><a class="btn btn-ghost" href="#quote">Request an estimate</a></div>
  </div>
</section>
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
<section class="section" style="padding-top:0"><div class="wrap">{tally_block()}</div></section>
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
<section class="page-hero" style="--hero: url('images/driveways-2.jpg')">
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Home</a> · Service areas</p>
    <h1>Concrete Service Areas around Youngstown</h1>
    <p>Concrete Youngstown works in Youngstown and the towns around it in Mahoning County and nearby Trumbull County. Each page below is about the flatwork on those lots: access, drainage, salt, and the kind of slab we are usually replacing. It is not a town history.</p>
    <div class="hero-actions"><a class="btn btn-red" href="tel:{PHONE_TEL}">Call {PHONE_DISP}</a></div>
  </div>
</section>
<section class="section"><div class="wrap"><div class="factors">{"".join(blocks)}</div></div></section>
<section class="section" style="padding-top:0">
  <div class="wrap prose">
    <h2>Youngstown itself</h2>
    <p>In the city, drives are often shorter, trucks have less room, and the concrete has already lived through a lot of salt. The service pages for <a href="concrete-driveways.html">driveways</a>, <a href="concrete-patios.html">patios</a>, <a href="stamped-concrete.html">stamped concrete</a>, <a href="stained-concrete.html">stained concrete</a>, <a href="asphalt-paving.html">asphalt</a>, and <a href="concrete-installation.html">other flatwork</a> are written for that work. If your street is in Youngstown, start there or send the form.</p>
  </div>
</section>
<section class="section" style="padding-top:0"><div class="wrap">{tally_block()}</div></section>
"""
    page(
        "service-areas.html",
        "Concrete Service Areas near Youngstown, Ohio",
        "Concrete and asphalt flatwork in Youngstown, Boardman, Austintown, Canfield, Poland, Struthers, Warren, Niles, Girard, Hubbard, and Campbell.",
        body,
        SITE + "/service-areas.html",
        SITE + "/images/driveways-2.jpg",
        crumbs_schema([("Home", ""), ("Service areas", "service-areas.html")]),
    )


def about():
    body = f"""
<section class="page-hero" style="--hero: url('images/services.jpg')">
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Home</a> · About</p>
    <h1>About Concrete Youngstown</h1>
    <p>We are a service-area concrete crew for Youngstown and the towns around it. Driveways, patios, stamped and stained flatwork, sidewalks, small pads, and asphalt paving. There is no showroom and no public storefront. The estimate starts with the slab you have.</p>
    <div class="hero-actions"><a class="btn btn-red" href="tel:{PHONE_TEL}">Call {PHONE_DISP}</a><a class="btn btn-ghost" href="contact.html">Contact</a></div>
  </div>
</section>
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
<section class="section" style="padding-top:0"><div class="wrap">{tally_block()}</div></section>
"""
    page(
        "about.html",
        "About Concrete Youngstown | Youngstown, Ohio",
        "Concrete Youngstown is a service-area crew for driveways, patios, decorative flatwork, and asphalt in Youngstown, Ohio. Call (330) 293-2914.",
        body,
        SITE + "/about.html",
        SITE + "/images/services.jpg",
        crumbs_schema([("Home", ""), ("About", "about.html")]),
    )


def contact():
    body = f"""
<section class="page-hero" style="--hero: url('images/installation-1.jpg')">
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Home</a> · Contact</p>
    <h1>Request a Concrete Estimate</h1>
    <p>Call <a class="inline" href="tel:{PHONE_TEL}">{PHONE_DISP}</a> or use the form. Include the city, whether this is a new pour or a replacement, and roughly what the slab is for. We schedule a look before we price it.</p>
  </div>
</section>
<section class="section"><div class="wrap">{tally_block()}</div></section>
"""
    page(
        "contact.html",
        "Contact Concrete Youngstown | Free Concrete Estimate",
        "Call (330) 293-2914 or request a concrete estimate in Youngstown, Ohio. Driveways, patios, stamped concrete, stain, and asphalt.",
        body,
        SITE + "/contact.html",
        SITE + "/images/installation-1.jpg",
        crumbs_schema([("Home", ""), ("Contact", "contact.html")]),
    )


def faq_page():
    all_items = HOME_FAQS + MORE_FAQS
    body = f"""
<section class="page-hero" style="--hero: url('images/patios-1.jpg')">
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Home</a> · FAQs</p>
    <h1>Concrete Questions in Youngstown</h1>
    <p>Straight answers about cost, replacement, decorative finishes, and where we work. Service pages have more specific questions for that slab.</p>
    <div class="hero-actions"><a class="btn btn-red" href="tel:{PHONE_TEL}">Call {PHONE_DISP}</a></div>
  </div>
</section>
<section class="section"><div class="wrap">{faq_html(all_items)}
  <p>Looking for a single service? Read the <a href="concrete-driveways.html">driveway</a>, <a href="concrete-patios.html">patio</a>, <a href="stamped-concrete.html">stamped</a>, <a href="stained-concrete.html">stained</a>, <a href="asphalt-paving.html">asphalt</a>, or <a href="concrete-installation.html">installation</a> page.</p>
</div></section>
<section class="section" style="padding-top:0"><div class="wrap">{tally_block()}</div></section>
"""
    page(
        "faq.html",
        "Concrete FAQs for Youngstown, Ohio | Concrete Youngstown",
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
