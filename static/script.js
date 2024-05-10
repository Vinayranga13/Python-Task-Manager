function changeTheme(theme) {
    let bgColor, textColor;
    switch (theme) {
        case 'orange':
            bgColor = '#DC6D18';
            textColor = 'white';
            break;
        case 'ivory':
            bgColor = '#FFF4E4';
            textColor = 'black';
            break;
        case 'cream':
            bgColor = '#F8E0C9';
            textColor = 'black';
            break;
        case 'black':
            bgColor = '#2B1A12';
            textColor = 'white';
            break;
        case 'limestone':
            bgColor = '#B1AA81';
            textColor = 'black';
            break;
        default:
            bgColor = '#f5f5f5';
            textColor = 'black';
    }

    document.body.style.backgroundColor = bgColor;
    document.body.style.color = textColor;
}

function markDone(taskId) {
}