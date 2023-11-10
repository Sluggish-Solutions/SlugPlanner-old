<script>
	import {Button} from "$lib/components/ui/button";
</script>

<header class="flex p-6 h-auto">
	<nav class = " justify-start items-start">
		<a href="/">
			<!-- change logo dark/light mode -->
			<h1 class = "font-bold text-5xl p-5 pl-9 underline decoration-yellow-300 decoration-4">SlugPlanner</h1>
		</a>
	</nav>
	
	<nav class=" flex w-full">
		<!-- left section -->
		

		<!-- middle section -->
		<ul
			class="flex justify-evenly items-center font-medium space-x-7 py-10 min-w-[25rem] w-full"
		>
			<li><a href="/class">classes</a></li>
			<li><a href="/login">login</a></li>
			<li><a href="/signup">logout</a></li>
			<li><a href="/about_us">About Us</a></li>
			<!-- <li class='flex items-center'>
				<a href="/contact">Contact</a>
				<CaretRight class="h-[1.5rem] w-[1.5rem]"/>
			</li> -->
		</ul>

		<!-- right section -->
		<div
			id="right"
			class="rounded-md w-52 pl-2 flex justify-between items-center"
		>

				
		</div>
	</nav>

</header>