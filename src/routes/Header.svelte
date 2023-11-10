<script>
	import {Button} from "$lib/components/ui/button";
</script>

<header class="flex items-center justify-center p-6 h-[10vh]">
	<nav class="flex justify-between items-center">
		<!-- left section -->
		<a href="/">
			<!-- change logo dark/light mode -->
			<h1>Home!</h1>
		</a>

		<!-- middle section -->
		<ul
			class="flex justify-evenly items-center font-medium space-x-7 min-w-[25rem]"
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