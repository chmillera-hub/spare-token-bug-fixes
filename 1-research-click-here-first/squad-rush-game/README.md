# Squad Rush game

Squad Rush is a free phone game that runs in a web browser and an AI chatbot (Claude Fable 5.2) wrote the whole game from prompts in a chat.

## Play the game

Tap this address on a phone or a computer to play because the game needs no download and no account: https://chmillera-hub.github.io/spare-token-bug-fixes/1-research-click-here-first/squad-rush-game/play.html

A second copy of the game lives on claude.ai at this address: https://claude.ai/artifact/TTDq6L9H1QE9Wsm1AsecaW

Both addresses run the same version of the game because the author shared the claude.ai copy with the public.

## How the game works

A squad of blue soldiers runs up a road and shoots without any button while a thumb drags the squad left and right. The game copies the style of the lane shooter commercials that show up between mobile games.

- Blue number gates add soldiers and red enemies remove a soldier with each touch.
- Each row of bonus gates gives the squad one pick so the player chooses between more soldiers or a multiplier or faster firing or more damage or blast rounds or an ally.
- Enemies never walk on a conveyor belt so a squad that camps on the belt shoots at nothing and gets swarmed from the side.
- Yellow cages hold special units: a Laser Gunner and a Flamethrower and a Blade Thrower whose blade bounces off the road walls and a Rocketeer and a Frost Mage who slows enemies.
- Ten stages each add one trick such as barrels with prizes and gates that rise when shot and saws and giants and a boss with 50000 HP.
- Every stage has turrets of three kinds: an orange turret fires straight down the road and a purple turret marked x3 fires a fan of three shells and a red turret marked AIM fires at the spot where the squad stood at the moment of firing.
- Most bonus rows and several prize barrels slide side to side so the player steers the squad to line up with the wanted bonus and a player who looks away can miss a bonus.
- Spikes sit on some conveyor belts and beside some bonus rows so the squad hops off a belt and back on.
- Each stage opens on a start card with the instructions and the stage stays frozen until the player taps Start.

## What was tested and what was not

A scripted player ran every stage 20 to 40 times and won between 2 of 20 runs and 20 of 20 runs depending on the stage while a squad that never moved lost every stage. The scripted player dodges shells worse than a person does so a person could win more often than the scripted player did. The chatbot also looked at screenshots in a phone-sized browser window. The chatbot could not hear the music or the sound effects and could not hold a real phone so the sound balance and the frame rate on a real phone are untested.

## Files

- [play.html](play.html) is the whole game in one file (drawing code and music code and all ten stages) so anyone may download the file and open the file in a browser or change the stages.
