[h1]Unlimited Buildings & Megastructures[/h1]

The development version of this mod would post on [url=https://github.com/Lyther/UnlimitedBuildings]GitHub[/url]. If you want to play the latest version instead of the stable version, please follow the repo and use [code]git pull[/code] to get the latest commit.

Having a limit on the number of buildings of the same type is just stupid! Sadly, we can build unlimited research labs, but not as many research centers.

When I build a smelting planet, I end up with a lone nano-alloy furnace, and the rest of the place is filled with forts/research labs/rare resource factories. Why not let smelting planets have an unlimited number of alloy furnaces?

The same goes for the megastructure, over a planet where a star ring base is built, empty space is simply too good to put a habitable station, but the vanilla mechanism does not allow this. After the space civilization built the Dyson sphere, it is surprising that it would freeze all the habitable spheres in the galaxy, is it surprising that the FTL civilization does not have artificial light sources and other technologies? Likewise, after building habitation stations on planets, dead-brained scientists can't imagine that they can build sentinel arrays next to habitation stations, which they believe have crowded out the space where other megastructures would have been built, so they refuse to build other megastructures on planets where they were built.

What's even more puzzling is that megastructures have a limit of one per megastructure, and even with more resources, players cannot continue to build more Dyson Spheres and Matter Decompressors, which is obviously unconscionable.

Therefore, the reform of the megastructure building is imperative.

[h2]Building Unlock[/h2]

Now we can build an unlimited number of various buildings! Including.

[list]
[*] Various planet buildings from the original version, research centers, psychic legions, factories, etc.
[*] Various buildings of the Corporate Branch Office can be filled with smuggling ports in the branch office.
[*] Overlord buildings, where the scientific research department's glory returns.
[*] Population assembly buildings, robots to assemble more and more.
[*] Lifted a series of construction restrictions on megastructures (e.g. number of stacks, clearing galaxies after construction, etc.).
[/list]

Buildings that are not included in the infinite buildings are.

[list]
[*] Cultural centers purchased by the Art Association (only one can be built after buying only one).
[*] Starbase components (haven't found a way to build multiple hydroponic pods or fleet academies yet).
[/list]

[h2]Megastructure[/h2]

All megastructures can be built with no upper limit on the number of buildings, but the limit on the number of simultaneous builds still follows the original mechanism.

[list]
[*] Ring World: Unlocked the limit of building galaxies (double stars, triple stars, black holes), the building will not affect other planets in the galaxy, will not empty the galaxy when finished, and can be stacked infinitely.
[*] Dyson Sphere: Unlocked the limit of building galaxies (binary stars, triple stars, black holes), construction will not affect planets in the galaxy, all habitable spheres are preserved and can be stacked infinitely.
[*] All Planetary Star Mega Constructs: Can be built on planets' moons and stacked infinitely.
[*] Matter Decompressor: Can be stacked indefinitely.
[*] Habitable Stations: Can be built on a planet's moons, stacked infinitely, and built on sectors of ringworlds.
[/list]

[h2]Script Usage[/h2]

[code]remove_building_limits.py[/code]

This script automates the process of generating modified building files to remove the limitations on the number of buildings you can construct in the game. It is designed to be simple and efficient, requiring minimal input from the user.

[h3]Requirements[/h3]

[list]
[*] Python 3.x
[*] Game building files in [.txt] format
[/list]

[h3]Instructions[/h3]

[list=1]
[*] Gather all the building [.txt] files that you wish to modify and place them in a single directory (this will be your input directory).
[*] Ensure Python 3.x is installed on your system.
[*] Open a terminal or command prompt window.
[*] Navigate to the directory where the script is located.
[*] Run the script with the following command, replacing [i]<input_folder>[/i] with the path to your input directory and [i]<output_folder>[/i] with the path to your desired output directory:
[code]python3 remove_building_limits.py <input_folder> <output_folder>[/code]
[*] The script will process each [.txt] file and generate a new version without building limits in the specified output directory.
[*] Once the script has finished running, copy all the files from the output directory to the [i]common/buildings[/i] folder within your game directory.
[/list]

[h3]Example[/h3]

If your input directory is [i]C:\mods\input_buildings[/i] and your output directory is [i]C:\mods\output_buildings[/i], the command would be:

[code]python3 remove_building_limits.py C:\mods\input_buildings C:\mods\output_buildings[/code]

[h2]Updates/compatibility[/h2]

If a new version of the game is released or you want to be compatible with an older version, you can leave a comment or private message in the Creative Workshop.

If you have more ideas for mod compatibility, or want to make other mods' buildings infinitely buildable, you can also leave a message in the Creative Workshop.

The compatible mods for Infinite Buildings have been split, if you subscribe to other mods, you can subscribe to Infinite Buildings compatible patches for this mod at the same time, all the Infinite Buildings compatible patches will be in the Creative Factory collection.

[b]Please note: You need to place the infinite buildings compatibility patch under the compatibilized mod when sorting.[/b]

[h1]无限建筑&巨构[/h1]

此MOD的开发版本将在 [url=https://github.com/Lyther/UnlimitedBuildings]GitHub[/url] 进行实时更新，如果您想游玩最新的开发版本而非稳定版本，可以通过GitHub仓库的[code]git pull[/code]获取最新的commit。

同类型的建筑有数量限制实在是太蠢了！我们可以建造数量无限的研究实验室，但是却不能建造同样多的研究中心，实在是一件很令人伤心的事情。

当我建设了一个冶炼星球，结果却只有一个孤零零的纳米合金熔炉，余下的地方都放满了堡垒/研究实验室/稀有资源工厂。为什么不让冶炼星球拥有数量无限的合金熔炉？

巨构建筑也是同理，在一个建造了星环基地的星球上空，空荡荡的太空简直太适合放一个居住站了，但是原版的机制中并不允许这么做。太空文明建设了戴森球之后，竟然会冻结星系里的所有宜居球，难道超光速文明竟然没有人造光源之类的科技吗？同样的，在星球上建造了居住站之后，死脑筋的科学家们想不到它们可以把哨兵阵列建设在居住站旁边，它们认为居住站已经挤占了原本建设其他巨构的空间，因此它们拒绝在建造了巨构的星球上建造其他巨构。

更令人费解的是，巨构建筑拥有每种巨构只能建造一个的限制，即便拥有再多资源，玩家也无法继续建设更多的戴森球和物质解压器，这显然是不合常理的。

因此，巨构建筑的改革势在必行。

[h2]建筑解锁[/h2]

现在，我们可以建造数量无限的各种建筑了！包括：

[list]
[*] 原版的各种星球建筑，研究中心、灵能军团、工厂等；
[*] 企业分部的各种建筑，当然可以在分部里开满走私港；
[*] 宗主建筑，科研部的荣光再次回归；
[*] 人口组装建筑，机器人组装多多益善；
[*] 解除了巨构建筑的一系列建造限制（如数量堆叠、建造后清空星系等）。
[/list]

不包含在无限建筑中的建筑有：

[list]
[*] 艺术协会购买的文化中心（只买了一座就只能建造一座）；
[*] 恒星基地组件（暂时没找到建造多个水培舱、舰队学院的办法）。
[/list]

[h2]巨构建筑[/h2]

全部巨构建筑均可以无数量上限建造，但同时建造的数量限制仍然遵循原版机制。

[list]
[*] 环形世界：解锁了建造星系限制（双恒星、三恒星、黑洞），建造不会影响星系内其他星球，建造完成不会清空星系，可以无限堆叠。
[*] 戴森球：解锁了建造星系限制（双恒星、三恒星、黑洞），建造完成后不会影响星系内行星，宜居球全部保留，可以无限堆叠。
[*] 所有行星级巨构：可以在星球的卫星上建造，可以无限堆叠。
[*] 物质解压器：可以无限堆叠。
[*] 居住站：可以在星球的卫星上建造，可以无限堆叠，可以在环形世界的区段上建造。
[/list]

[h2]脚本使用说明[/h2]

[code]remove_building_limits.py[/code]

该脚本自动化生成修改过的建筑文件的过程，以移除游戏中建筑数量的限制。它的设计简单高效，用户只需提供最少的输入。

[h3]要求[/h3]

[list]
[*] Python 3.x
[*] 游戏建筑文件 [.txt] 格式
[/list]

[h3]使用指南[/h3]

[list=1]
[*] 收集所有你希望修改的建筑 [.txt] 文件，并将它们放置在一个文件夹中（这将是你的输入文件夹）。
[*] 确保你的系统已安装 Python 3.x。
[*] 打开一个终端或命令提示符窗口。
[*] 导航到脚本所在的目录。
[*] 使用以下命令运行脚本，将 [i]<input_folder>[/i] 替换为你的输入文件夹路径，将 [i]<output_folder>[/i] 替换为你希望输出的文件夹路径：
[code]python3 remove_building_limits.py <input_folder> <output_folder>[/code]
[*] 脚本将处理每一个 [.txt] 文件，并在指定的输出目录生成一个无建筑限制的新版本。
[*] 脚本运行完成后，将所有文件从输出目录复制到游戏目录中的 [i]common/buildings[/i] 文件夹。
[/list]

[h3]示例[/h3]

如果你的输入文件夹是 [i]C:\mods\input_buildings[/i] 而输出文件夹是 [i]C:\mods\output_buildings[/i]，命令将会是：

[code]python3 remove_building_limits.py C:\mods\input_buildings C:\mods\output_buildings[/code]

[h2]更新/兼容[/h2]

如果有新的游戏版本发布，或是希望与一个更老的游戏版本兼容，你可以在创意工坊留言或是私信沟通。

如果你有更多的MOD兼容想法，或者希望让其他MOD的建筑也能无限建造，同样可以在创意工坊留言。

无限建筑的兼容MOD已经拆分，如果你订阅了其他的MOD，可以同时订阅无限建筑对于此MOD的兼容补丁，全部的无限建筑兼容补丁将会在创意工厂的合集中。

[b]请注意：排序时需要将无限建筑的兼容补丁放置于兼容MOD之下。[/b]
