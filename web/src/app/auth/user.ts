export interface User {
    id: number;
    username: string;
    first_name: string;
    last_name: string;
    email: string;
    date_joined: Date;
    last_login: Date;
    is_active: boolean;
    is_staff: boolean;
    is_superuser: boolean;
}
