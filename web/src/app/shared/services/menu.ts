export interface MenuMeta {
    title: string;
    icon?: string;
    url?: string;
    children?: MenuMeta[];
}

export class Menu {

    private static _instance: Menu;
    private _menuList: MenuMeta[];

    public static get instance(): Menu {
        if (!this._instance) {
            this._instance = new Menu();
        }
        return this._instance;
    }

    constructor() {
        this._menuList = [];
    }

    get menuList() {
        return this._menuList;
    }

    addMenu(menu: MenuMeta) {
        this._menuList.push(menu);
    }

}
