import { supabase } from "$lib/backend/supabaseClient";

export const signUpUser = async (email:string, password:string) => {
    const { data, error} = await supabase.auth.signUp({
        email: email,
        password: password
    })

    console.log(data)

}