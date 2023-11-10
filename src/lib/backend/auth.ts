import { supabase } from "$lib/backend/supabaseClient";

export interface SignUpResult {
  data?: any; // You might want to replace 'any' with the actual type of data returned by Supabase
  error?: any; // You might want to replace 'any' with the actual type of error returned by Supabase
}

export const signUpUser = async (email: string, password: string): Promise<SignUpResult> => {
  try {
    const { data, error } = await supabase.auth.signUp({
      email: email,
      password: password,
    });

    // console.log(data);

    return { data, error };
  } catch (error) {
    return { error }; // Handle unexpected errors
  }
};
