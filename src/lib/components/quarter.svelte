<script lang="ts">
    export let quarter_year: string = "todo";
    export let class1: string = "todo";
    export let class2: string = "todo";
    export let class3: string = "todo";
    export let class4: string = "todo";
</script>

<div class="rounded-xl flex-grow w-auto px-1 flex flex-col items-center border bg-card text-card-foreground shadow">
    <!-- quarter_year appears on top -->
    <h1 class="text-xl font-semibold mt-2 text-center">{quarter_year}</h1>
    <!-- Rest of the content -->
    <div class=" text-center p-1">
        <a href="class/{class1}"><h1 class="p-1">{class1}</h1></a>
        <h1 class="p-1">{class2}</h1>
        <h1 class="p-1">{class3}</h1>
        <h1 class="p-1">{class4}</h1>
    </div>
</div>


