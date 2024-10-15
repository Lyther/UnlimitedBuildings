# Unlimited Buildings & Megastructures

The development version of this mod is available on [GitHub](https://github.com/Lyther/UnlimitedBuildings) for real-time updates. If you want to play the latest development version instead of the stable release, you can use `git pull` to get the latest commit from the GitHub repository.

Having a limit on the number of buildings of the same type is absurd! We can build unlimited research labs, but can't build as many research centers, which is frustrating.

When I build a smelting planet, I end up with a lone nano-alloy furnace, while the rest of the space is filled with fortresses, research labs, and rare resource factories. Why not allow smelting planets to have unlimited alloy furnaces?

The same goes for megastructures. In the vanilla game, over a planet with a star ring base, the empty space is perfect for placing a habitable station, yet the game doesn't allow it. After a Dyson Sphere is built, it freezes all habitable planets in the system, as if a faster-than-light civilization lacks artificial lighting and other technologies! Similarly, once habitation stations are built, stubborn scientists cannot imagine constructing sentinel arrays next to them because they believe the habitation stations occupy the space for other megastructures, refusing to allow any additional constructions.

Even more baffling is the limitation of one megastructure per type. No matter how many resources you have, players cannot build more Dyson Spheres or Matter Decompressors, which is illogical.

Therefore, a reform of the megastructure system is essential.

## Building Unlock

Now, we can build unlimited numbers of various buildings, including:

* All original planetary buildings such as research centers, psychic legions, and factories.
* Various Corporate Branch Office buildings, allowing branch offices to be filled with smuggling ports.
* Overlord buildings, bringing back the glory of the Science Department.
* Population assembly buildings—assemble as many robots as you want.
* A series of construction restrictions on megastructures has been lifted (e.g., stacking limit, galaxy clearing upon completion, etc.).

Buildings not included in the unlimited build list are:

* Cultural centers purchased from the Art Association (only one can be built after purchasing one).
* Starbase components (so far, there is no way to build multiple hydroponic bays or fleet academies).

## Megastructures

All megastructures can be built without an upper limit on the number of constructions, though the limit on simultaneous builds still follows the original game mechanics.

> If you don't need this feature, delete the `common/megastructures` folder in the mod directory.

* Ring World: Unlocked the limit on building in galaxy types (binary stars, triple stars, black holes), construction won't affect other planets in the system, won't clear the galaxy upon completion, and can be stacked infinitely.
* Dyson Sphere: Unlocked the limit on building in galaxy types (binary stars, triple stars, black holes), construction won't affect planets in the system, all habitable planets are preserved, and it can be stacked infinitely.
* Matter Decompressor: Unlocked the limit on building in galaxy types (binary stars, triple stars, black holes), and it can be stacked infinitely.
* All Planetary Star Megastructures: Can be built on planetary moons and stacked infinitely.
* Habitable Stations: Can be built on planetary moons, stacked infinitely, and built on ringworld sections. Research, energy, mining districts, and rare resource gathering buildings are all unlocked by default.
* Star Ring Base: Can be built on uncolonized habitable planets or restored on previously uncolonized planets.

**Note: Most megastructures allow AI empires to only build one; in rare cases, AI empires (especially Fallen Empires) may still build multiple megastructures.**

## Updates/Compatibility

If a new game version is released or you wish to be compatible with an older version, you can leave a comment or private message in the Steam Workshop.

If you have more ideas for mod compatibility or want other mods' buildings to be buildable without limits, feel free to leave a message in the Steam Workshop.

The compatible mods for Unlimited Buildings have been split into separate files. You can find a `compatibility` folder within the mod directory, containing compatibility patches for supported mods. You can replace the necessary files as needed (ensure you have the prerequisite mods installed to use Unlimited Buildings' compatibility features). **Typically, the mod directory is located at `Steam/steamapps/workshop/content/281990/2846706267`.**

**Please note: When sorting mods, place Unlimited Buildings below other mods that require compatibility.**

### Automatic Mod Compatibility

The `remove_building_limits.py` file in the mod directory is used to automatically remove building limits. The script performs simple regular expression replacements, which works for most cases. When using it, specify the input folder (the building folder where you want to remove limits) and the output folder (where the modified files will be placed). Move the files from the output folder to `common/buildings` to complete compatibility.

If you've added compatibility for more mods, your pull requests are very welcome and much appreciated.

# 无限建筑&巨构

此MOD的开发版本将在[GitHub](https://github.com/Lyther/UnlimitedBuildings)进行实时更新，如果您想游玩最新的开发版本而非稳定版本，可以通过GitHub仓库的`git pull`获取最新的commit。

同类型的建筑有数量限制实在是太蠢了！我们可以建造数量无限的研究实验室，但是却不能建造同样多的研究中心，实在是一件很令人伤心的事情。

当我建设了一个冶炼星球，结果却只有一个孤零零的纳米合金熔炉，余下的地方都放满了堡垒/研究实验室/稀有资源工厂。为什么不让冶炼星球拥有数量无限的合金熔炉？

巨构建筑也是同理，在一个建造了星环基地的星球上空，空荡荡的太空简直太适合放一个居住站了，但是原版的机制中并不允许这么做。太空文明建设了戴森球之后，竟然会冻结星系里的所有宜居球，难道超光速文明竟然没有人造光源之类的科技吗？同样的，在星球上建造了居住站之后，死脑筋的科学家们想不到它们可以把哨兵阵列建设在居住站旁边，它们认为居住站已经挤占了原本建设其他巨构的空间，因此它们拒绝在建造了巨构的星球上建造其他巨构。

更令人费解的是，巨构建筑拥有每种巨构只能建造一个的限制，即便拥有再多资源，玩家也无法继续建设更多的戴森球和物质解压器，这显然是不合常理的。

因此，巨构建筑的改革势在必行。

## 建筑解锁

现在，我们可以建造数量无限的各种建筑了！包括：

* 原版的各种星球建筑，研究中心、灵能军团、工厂等；
* 企业分部的各种建筑，当然可以在分部里开满走私港；
* 宗主建筑，科研部的荣光再次回归；
* 人口组装建筑，机器人组装多多益善；
* 解除了巨构建筑的一系列建造限制（如数量堆叠、建造后清空星系等）。

不包含在无限建筑中的建筑有：

* 艺术协会购买的文化中心（只买了一座就只能建造一座）；
* 恒星基地组件（暂时没找到建造多个水培舱、舰队学院的办法）。

## 巨构建筑

全部巨构建筑均可以无数量上限建造，且不再有同时建造的数量限制。

> 如果您不需要此功能，请在MOD目录下删除`common/megastructures`文件夹。

* 环形世界：解锁了建造星系限制（双恒星、三恒星、黑洞），建造不会影响星系内其他星球，建造完成不会清空星系，可以无限堆叠。
* 戴森球：解锁了建造星系限制（双恒星、三恒星、黑洞），建造完成后不会影响星系内行星，宜居球全部保留，可以无限堆叠。
* 物质解压器：解锁了建造星系限制（双恒星、三恒星、黑洞），可以无限堆叠。
* 所有行星级巨构：可以在星球的卫星上建造，可以无限堆叠。
* 居住站：可以在星球的卫星上建造，可以无限堆叠，可以在环形世界的区段上建造，默认解锁研究、发电、采矿区划，且可以建造稀有资源采集建筑。
* 星环基地：可以在无人居住的宜居球上建造，或是修复未殖民星球上的星环基地。

**注意：大部分的巨构建筑仅允许AI帝国建造一个，少数情况下仍会出现AI帝国（尤其是复兴帝国）建造多个巨构的现象。**

## 更新/兼容

如果有新的游戏版本发布，或是希望与一个更老的游戏版本兼容，你可以在创意工坊留言或是私信沟通。

如果你有更多的MOD兼容想法，或者希望让其他MOD的建筑也能无限建造，同样可以在创意工坊留言。

无限建筑的兼容MOD已经拆分，您可以在MOD目录下找到名为`compatibility`的文件夹，内部为所支持的MOD。您可以根据自己的需要自行进行覆盖（需要安装前置MOD，才能正常使用无限建筑的兼容性功能）。**通常而言，MOD目录位于`Steam/steamapps/workshop/content/281990/2846706267`。**

**请注意：排序时需要将无限建筑放置于其他需要兼容的MOD之下。**

### 自动进行MOD兼容

在MOD目录下的`remove_building_limits.py`文件用于自动移除建筑的数量限制，脚本只进行简单的正则表达式替换，大多数情况足以胜任。使用时需要指定输入文件夹（需要移除限制的建筑文件夹）和输出文件夹（移除后的文件会放置在里面）。将输出文件夹中的文件移动进`common/buildings`即可完成兼容。

如果您完成了更多MOD的兼容性，非常荣幸能得到您的pull requests，十分感谢。